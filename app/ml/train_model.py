import os
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).resolve().parents[2])
sys.path.append(project_root)

import pandas as pd
import numpy as np
from app import create_app, db
from app.models import Ticket
from app.ml.preprocessor import TicketClassifier


def train_classifier():
    """Train and save the ticket classifier"""
    # Create the ML directory if it doesn't exist
    ml_dir = os.path.dirname(__file__)
    os.makedirs(ml_dir, exist_ok=True)

    app = create_app()

    with app.app_context():
        # Get all tickets from database
        tickets = Ticket.query.all()

        if not tickets:
            raise ValueError("No tickets found in database. Please run init_db.py first.")

        # Convert to DataFrame
        df = pd.DataFrame([{
            'ticket_subject': ticket.ticket_subject,
            'ticket_description': ticket.ticket_description,
            'ticket_type': ticket.ticket_type,
            'product_purchased': ticket.product_purchased if hasattr(ticket, 'product_purchased') else None
        } for ticket in tickets])

        print(f"Total tickets loaded for training: {len(df)}")
        print("\nSample size per ticket type:")
        type_counts = df['ticket_type'].value_counts()
        for ticket_type, count in type_counts.items():
            print(f"- {ticket_type}: {count} tickets")

        # Initialize and train classifier
        classifier = TicketClassifier()
        results = classifier.train(df)

        # Save the model
        classifier.save_model()

        print("\nTraining Results:")
        print(f"Training Accuracy: {results['train_accuracy']:.2%}")
        print(f"Test Accuracy: {results['test_accuracy']:.2%}")
        print(f"Cross-validation Mean Accuracy: {results['cv_scores_mean']:.2%}")
        print(f"Cross-validation Std: {results['cv_scores_std']:.2%}")

        print("\nPer-class Performance:")
        for class_name, accuracy in results['class_accuracies'].items():
            samples = results['class_samples'][class_name]
            print(f"- {class_name}: {accuracy:.2%} (samples in test set: {samples})")

        if results['feature_importance']:
            print("\nTop 10 Most Important Features:")
            sorted_features = sorted(
                results['feature_importance'].items(),
                key=lambda x: x[1],
                reverse=True
            )[:10]
            for feature, importance in sorted_features:
                print(f"- {feature}: {importance:.4f}")

        return results


if __name__ == '__main__':
    try:
        results = train_classifier()
    except Exception as e:
        print(f"Error during training: {str(e)}")