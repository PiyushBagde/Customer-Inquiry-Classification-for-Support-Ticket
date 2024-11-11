import re
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os

# Download required NLTK data
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')


class TicketClassifier:
    def __init__(self):
        self.pipeline = None
        self.label_encoder = LabelEncoder()
        self.model_path = os.path.join(os.path.dirname(__file__), 'ticket_classifier.pkl')
        self.vectorizer_path = os.path.join(os.path.dirname(__file__), 'tfidf_vectorizer.pkl')
        self.label_encoder_path = os.path.join(os.path.dirname(__file__), 'label_encoder.pkl')

    def preprocess_text(self, text):
        """Clean and preprocess text data"""
        # Convert to lowercase
        text = text.lower()

        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)

        # Tokenization
        tokens = word_tokenize(text)

        # Remove stopwords and lemmatize
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]

        return ' '.join(tokens)

    def combine_features(self, subject, description):
        """Combine subject and description with appropriate weighting"""
        # Give more weight to the subject by repeating it
        return f"{subject} {subject} {description}"

    def prepare_data(self, df):
        """Prepare the data for training"""
        # Combine subject and description
        X = [self.combine_features(
            self.preprocess_text(subject),
            self.preprocess_text(desc)
        ) for subject, desc in zip(df['ticket_subject'], df['ticket_description'])]

        # Encode labels
        y = self.label_encoder.fit_transform(df['ticket_type'])

        return X, y

    def train(self, df, test_size=0.2):
        """Train the classifier"""
        # Prepare data
        X, y = self.prepare_data(df)

        # Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )

        # Create pipeline
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(
                max_features=5000,
                ngram_range=(1, 2),
                min_df=2
            )),
            ('classifier', LogisticRegression(
                multi_class='multinomial',
                max_iter=1000,
                random_state=42
            ))
        ])

        # Train the model
        self.pipeline.fit(X_train, y_train)

        # Calculate accuracy
        train_accuracy = self.pipeline.score(X_train, y_train)
        test_accuracy = self.pipeline.score(X_test, y_test)

        return {
            'train_accuracy': train_accuracy,
            'test_accuracy': test_accuracy,
            'num_classes': len(self.label_encoder.classes_),
            'classes': self.label_encoder.classes_.tolist()
        }

    def predict(self, subject, description):
        """Predict ticket type for new data"""
        if self.pipeline is None:
            raise ValueError("Model not trained yet!")

        # Preprocess and combine features
        text = self.combine_features(
            self.preprocess_text(subject),
            self.preprocess_text(description)
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