import re
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os

# Download required NLTK data
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class TicketClassifier:
    def __init__(self):
        self.pipeline = None
        self.label_encoder = LabelEncoder()
        self.model_path = os.path.join(os.path.dirname(__file__), 'ticket_classifier.pkl')
        self.label_encoder_path = os.path.join(os.path.dirname(__file__), 'label_encoder.pkl')

    def preprocess_text(self, text):
        """Clean and preprocess text data"""
        # Convert to lowercase and handle None
        text = str(text or '').lower()

        # Keep some punctuation as it might be meaningful
        text = re.sub(r'[^a-z\s.,!?]', ' ', text)

        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)

        # Tokenization
        tokens = word_tokenize(text)

        # Remove stopwords and lemmatize
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()

        # Keep only tokens with length > 2 to remove noise
        tokens = [lemmatizer.lemmatize(token) for token in tokens
                  if token not in stop_words and len(token) > 2]

        return ' '.join(tokens)

    def combine_features(self, subject, description, product=None):
        """Combine features with appropriate weighting"""
        # Normalize inputs
        subject = self.preprocess_text(subject)
        description = self.preprocess_text(description)
        product = self.preprocess_text(product) if product else ''

        # Simple concatenation with single subject weight
        combined = f"{subject} {description}"
        if product:
            combined = f"{product} {combined}"

        return combined.strip()

    def prepare_data(self, df):
        """Prepare the data for training"""
        print("\nPreparing data...")
        print(f"Initial number of samples: {len(df)}")

        # Remove rows with missing or empty values
        df = df.dropna(subset=['ticket_subject', 'ticket_description', 'ticket_type'])
        df = df[df['ticket_subject'].str.strip().str.len() > 0]
        df = df[df['ticket_description'].str.strip().str.len() > 0]

        print(f"Samples after cleaning: {len(df)}")

        # Combine features
        X = [self.combine_features(
            subject, desc, prod
        ) for subject, desc, prod in zip(
            df['ticket_subject'],
            df['ticket_description'],
            df['product_purchased'] if 'product_purchased' in df.columns else [None] * len(df)
        )]

        # Encode labels
        y = self.label_encoder.fit_transform(df['ticket_type'])

        # Print class distribution
        unique_labels, counts = np.unique(y, return_counts=True)
        print("\nClass distribution:")
        for label, count in zip(self.label_encoder.classes_, counts):
            print(f"{label}: {count} samples ({count / len(df) * 100:.1f}%)")

        return X, y

    def train(self, df, test_size=0.2):
        """Train the classifier with cross-validation"""
        # Prepare data
        X, y = self.prepare_data(df)

        # Ensure minimum samples per class
        unique_counts = np.unique(y, return_counts=True)[1]
        if min(unique_counts) < 3:
            raise ValueError("Each class must have at least 3 samples for training")

        # Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42, stratify=y
        )

        # Create pipeline with stricter parameters
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(
                max_features=100,  # Significantly reduced features
                ngram_range=(1, 1),  # Only unigrams
                min_df=2,  # Term must appear in at least 2 documents
                max_df=0.8,  # Ignore terms that appear in >80% of docs
                sublinear_tf=True,
                strip_accents='unicode',
                norm='l2'
            )),
            ('classifier', MultinomialNB(
                alpha=2.0  # Increased smoothing parameter
            ))
        ])

        # Train the model
        self.pipeline.fit(X_train, y_train)

        # Perform cross-validation
        cv_scores = cross_val_score(self.pipeline, X, y, cv=5)

        # Calculate metrics
        train_accuracy = self.pipeline.score(X_train, y_train)
        test_accuracy = self.pipeline.score(X_test, y_test)

        # Calculate per-class metrics
        y_pred = self.pipeline.predict(X_test)
        class_accuracies = {}
        class_samples = {}

        for label in self.label_encoder.classes_:
            label_idx = self.label_encoder.transform([label])[0]
            mask = y_test == label_idx
            if any(mask):
                class_pred = y_pred[mask]
                class_true = y_test[mask]
                class_accuracies[label] = np.mean(class_pred == class_true)
                class_samples[label] = sum(mask)

        # Get feature names and their importance
        feature_importance = None
        try:
            feature_names = self.pipeline.named_steps['tfidf'].get_feature_names_out()
            feature_importance = {
                feature: np.exp(self.pipeline.named_steps['classifier'].feature_log_prob_).mean(axis=0)[i]
                for i, feature in enumerate(feature_names)
            }
        except:
            pass

        return {
            'train_accuracy': train_accuracy,
            'test_accuracy': test_accuracy,
            'cv_scores_mean': cv_scores.mean(),
            'cv_scores_std': cv_scores.std(),
            'num_classes': len(self.label_encoder.classes_),
            'classes': self.label_encoder.classes_.tolist(),
            'class_accuracies': class_accuracies,
            'class_samples': class_samples,
            'feature_importance': feature_importance
        }

    def predict(self, subject, description, product=None):
        """Predict ticket type for new data"""
        if self.pipeline is None:
            raise ValueError("Model not trained yet!")

        # Preprocess and combine features
        text = self.combine_features(
            self.preprocess_text(subject),
            self.preprocess_text(description),
            self.preprocess_text(product) if product else None
        )

        # Predict
        pred_idx = self.pipeline.predict([text])[0]
        probabilities = self.pipeline.predict_proba([text])[0]

        # Get prediction and confidence
        prediction = self.label_encoder.inverse_transform([pred_idx])[0]
        confidence = float(probabilities[pred_idx])

        return {
            'predicted_type': prediction,
            'confidence': confidence,
            'probabilities': {
                self.label_encoder.inverse_transform([i])[0]: float(prob)
                for i, prob in enumerate(probabilities)
            }
        }

    def save_model(self):
        """Save the trained model and related components"""
        if self.pipeline is None:
            raise ValueError("No trained model to save!")

        # Save pipeline
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.pipeline, f)

        # Save label encoder
        with open(self.label_encoder_path, 'wb') as f:
            pickle.dump(self.label_encoder, f)

    def load_model(self):
        """Load the trained model and related components"""
        if not all(os.path.exists(p) for p in [self.model_path, self.label_encoder_path]):
            raise FileNotFoundError("Model files not found!")

        # Load pipeline
        with open(self.model_path, 'rb') as f:
            self.pipeline = pickle.load(f)

        # Load label encoder
        with open(self.label_encoder_path, 'rb') as f:
            self.label_encoder = pickle.load(f)
