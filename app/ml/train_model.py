import os
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).resolve().parents[2])  # Go up two levels from ml/train_model.py
sys.path.append(project_root)

import pandas as pd
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
            'ticket_type': ticket.ticket_type
        } for ticket in tickets])

        print(f"Total tickets loaded for training: {len(df)}")
        print("\nTicket type distribution:")
        print(df['ticket_type'].value_counts())

        # Initialize and train classifier
        classifier = TicketClassifier()
        results = classifier.train(df)

        # Save the model
        classifier.save_model()

        print("\nTraining Results:")
        print(f"Training Accuracy: {results['train_accuracy']:.2%}")
        print(f"Test Accuracy: {results['test_accuracy']:.2%}")
        print(f"Number of classes: {results['num_classes']}")
        print("\nClasses:")
        for class_name in results['classes']:
            print(f"- {class_name}")

        return results


if __name__ == '__main__':
    try:
        results = train_classifier()
    except Exception as e:
        print(f"Error during training: {str(e)}")