from flask import Blueprint, request, jsonify, render_template
from .models import db, Ticket
from .ml.preprocessor import TicketClassifier
import os
from datetime import datetime, timedelta
from sqlalchemy import func
from collections import defaultdict, Counter

main = Blueprint('main', __name__)
classifier = TicketClassifier()

# Load the model when starting the app
if os.path.exists(classifier.model_path):
    classifier.load_model()


@main.route('/')
def submit_ticket():
    """Render the ticket submission form"""
    return render_template('submit_ticket.html')


@main.route('/tickets')
def manage_tickets():
    """Render the ticket management page"""
    ticket_type = request.args.get('type')
    status = request.args.get('status')

    query = Ticket.query

    if ticket_type:
        query = query.filter_by(ticket_type=ticket_type)
    if status:
        query = query.filter_by(status=status)

    tickets = query.order_by(Ticket.created_at.desc()).all()

    # Get category statistics
    categories = defaultdict(int)
    for ticket in tickets:  # Corrected loop to iterate over fetched tickets
        categories[ticket.ticket_type] += 1  # Count based on ticket_type attribute

    return render_template('tickets.html', tickets=tickets, categories=categories)


@main.route('/api/classify', methods=['POST'])
def classify_ticket():
    """Classify a new ticket"""
    data = request.json

    try:
        result = classifier.predict(data['ticket_subject'], data['ticket_description'])
        return jsonify({'success': True, 'prediction': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@main.route('/api/tickets', methods=['GET'])
def get_tickets():
    """Get filtered tickets"""
    try:
        ticket_type = request.args.get('type')
        status = request.args.get('status')

        query = Ticket.query

        if ticket_type:
            query = query.filter_by(ticket_type=ticket_type)
        if status:
            query = query.filter_by(status=status)

        tickets = query.order_by(Ticket.created_at.desc()).all()
        categories = defaultdict(int)
        for ticket in tickets:
            categories[ticket.ticket_type] += 1

        return jsonify({
            'success': True,
            'tickets': [ticket.to_dict() for ticket in tickets],
            'categories': dict(categories)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@main.route('/api/tickets', methods=['POST'])
def create_ticket():
    """Create a new ticket with automatic classification"""
    data = request.json

    try:
        prediction = classifier.predict(data['ticket_subject'], data['ticket_description'])

        ticket = Ticket(
            customer_name=data['customer_name'],
            customer_email=data['customer_email'],
            product_purchased=data['product_purchased'],
            ticket_subject=data['ticket_subject'],
            ticket_description=data['ticket_description'],
            ticket_type=prediction['predicted_type'],  # Access predicted_type directly
            status='unresolved'
        )

        db.session.add(ticket)
        db.session.commit()

        return jsonify({'success': True, 'ticket': ticket.to_dict(), 'classification': prediction})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@main.route('/api/tickets/<int:ticket_id>/status', methods=['PATCH'])
def update_ticket_status(ticket_id):
    """Update ticket status"""
    try:
        ticket = Ticket.query.get_or_404(ticket_id)
        data = request.json

        if 'status' in data and data['status'] in ['resolved', 'unresolved']:
            ticket.status = data['status']
            db.session.commit()

            return jsonify({'success': True, 'ticket': ticket.to_dict()})
        else:
            return jsonify({'success': False, 'error': 'Invalid status value'}), 400

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500  # Return 500 for server errors


@main.route('/dashboard')
def dashboard():
    """Render the dashboard page"""
    return render_template('dashboard.html')


@main.route('/api/dashboard-data')
def dashboard_data():
    """Get dashboard data"""
    try:
        # Get summary statistics
        total_tickets = Ticket.query.count()
        open_tickets = Ticket.query.filter_by(status='unresolved').count()
        resolved_tickets = Ticket.query.filter_by(status='resolved').count()

        # Get ticket type distribution
        ticket_types = db.session.query(
            Ticket.ticket_type,
            func.count(Ticket.ticket_id)
        ).group_by(Ticket.ticket_type).all()

        # Get product distribution
        products = db.session.query(
            Ticket.product_purchased,
            func.count(Ticket.ticket_id)
        ).group_by(Ticket.product_purchased).all()

        # Get ticket trends (last 7 days)
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=7)

        trends = db.session.query(
            Ticket.created_at,  # Get the full datetime instead of func.date
            func.count(Ticket.ticket_id)
        ).filter(
            Ticket.created_at >= start_date
        ).group_by(
            func.date(Ticket.created_at)  # Still group by date
        ).all()

        # Format the data for charts
        chart_data = {
            'ticket_types': {
                'labels': [t[0] for t in ticket_types],
                'data': [t[1] for t in ticket_types]
            },
            'products': {
                'labels': [p[0] for p in products],
                'data': [p[1] for p in products]
            },
            'trends': {
                'labels': [t[0].date().strftime('%Y-%m-%d') for t in trends],
                'data': [t[1] for t in trends]
            }
        }

        all_tickets = Ticket.query.all()
        all_text = ' '.join([ticket.ticket_subject + ' ' + ticket.ticket_description for ticket in all_tickets])
        word_count = Counter(all_text.lower().split())
        top_keywords = dict(word_count.most_common(10))

        return jsonify({
            'success': True,
            'summary': {
                'total_tickets': total_tickets,
                'open_tickets': open_tickets,
                'resolved_tickets': resolved_tickets
            },
            'charts': chart_data,
            "topKeywords": {
                'labels': list(top_keywords.keys()),
                'data': list(top_keywords.values())
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
