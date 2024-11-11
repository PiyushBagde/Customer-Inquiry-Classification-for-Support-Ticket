from . import db
from datetime import datetime


class Ticket(db.Model):
    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(120), nullable=False)
    customer_gender = db.Column(db.String(20))
    product_purchased = db.Column(db.String(100))
    date_of_purchase = db.Column(db.DateTime)
    ticket_type = db.Column(db.String(50))
    ticket_subject = db.Column(db.String(200), nullable=False)
    ticket_description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='unresolved')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'ticket_id': self.ticket_id,
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'customer_gender': self.customer_gender,
            'product_purchased': self.product_purchased,
            'date_of_purchase': self.date_of_purchase.strftime('%Y-%m-%d') if self.date_of_purchase else None,
            'ticket_type': self.ticket_type,
            'ticket_subject': self.ticket_subject,
            'ticket_description': self.ticket_description,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
