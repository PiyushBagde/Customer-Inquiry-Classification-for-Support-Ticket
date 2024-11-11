import pandas as pd
import random
from datetime import datetime, timedelta

# Define sample data components
CUSTOMER_NAMES = [
    "John Smith", "Emma Wilson", "Michael Brown", "Sarah Davis", "James Johnson",
    "Lisa Anderson", "Robert Taylor", "Jennifer Martinez", "William Thomas", "Maria Garcia"
]

EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]

PRODUCTS = [
    "Laptop Pro", "Smartphone X", "Tablet Elite", "Smart Watch", "Wireless Earbuds",
    "Desktop PC", "Gaming Console", "Security Camera", "Smart Speaker", "Fitness Tracker"
]

TICKET_TYPES = [
    "Technical Support",
    "Billing Issue",
    "Product Inquiry",
    "Return Request",
    "Account Access",
    "Shipping Problem",
    "Product Defect",
    "Feature Request"
]

# Sample templates for each ticket type
TICKET_TEMPLATES = {
    "Technical Support": {
        "subjects": [
            "Device not turning on",
            "Software keeps crashing",
            "Cannot connect to WiFi",
            "Screen display issues",
            "Battery draining quickly"
        ],
        "descriptions": [
            "My device won't start up after the recent update. I've tried restarting multiple times.",
            "The application crashes every time I try to open it. This started happening yesterday.",
            "Unable to connect to any WiFi network. The device doesn't detect any networks.",
            "The screen is showing strange colors and flickering frequently.",
            "Battery life has suddenly decreased, only lasting 2 hours on full charge."
        ]
    },
    "Billing Issue": {
        "subjects": [
            "Double charged for order",
            "Incorrect price charged",
            "Refund not received",
            "Subscription billing error",
            "Unknown charge on account"
        ],
        "descriptions": [
            "I was charged twice for my recent purchase. Order number: #12345",
            "The price charged is different from what was shown during checkout.",
            "I returned the item last week but haven't received my refund yet.",
            "My subscription is showing the wrong billing amount this month.",
            "There's a charge on my account that I don't recognize."
        ]
    },
    "Product Inquiry": {
        "subjects": [
            "Product compatibility question",
            "Feature availability",
            "Product comparison",
            "Warranty information",
            "Technical specifications"
        ],
        "descriptions": [
            "Will this product work with my existing setup? I have a [specific model].",
            "Does this model include the new feature announced last month?",
            "What are the main differences between model A and model B?",
            "I need detailed information about the warranty coverage.",
            "Could you provide the full technical specifications for this product?"
        ]
    },
    # Add more templates for other ticket types...
}


def generate_sample_tickets(num_tickets=100):
    tickets = []

    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)  # Last 6 months

    for _ in range(num_tickets):
        # Select ticket type and corresponding templates
        ticket_type = random.choice(TICKET_TYPES)
        template = TICKET_TEMPLATES.get(ticket_type, {
            "subjects": ["General inquiry"],
            "descriptions": ["General description"]
        })

        # Generate ticket data
        customer_name = random.choice(CUSTOMER_NAMES)
        email = f"{customer_name.lower().replace(' ', '.')}@{random.choice(EMAIL_DOMAINS)}"

        ticket = {
            "Customer Name": customer_name,
            "Customer Email": email,
            "Customer Gender": random.choice(["Male", "Female"]),
            "Product Purchased": random.choice(PRODUCTS),
            "Date of Purchase": (start_date + timedelta(days=random.randint(0, 180))).strftime("%Y-%m-%d"),
            "Ticket Type": ticket_type,
            "Ticket Subject": random.choice(template["subjects"]),
            "Ticket Description": random.choice(template["descriptions"])
        }
        tickets.append(ticket)

    return pd.DataFrame(tickets)


def main():
    # Generate sample tickets
    df = generate_sample_tickets(100)

    # Save to CSV
    import os
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    os.makedirs(data_dir, exist_ok=True)

    csv_path = os.path.join(data_dir, 'sample_tickets.csv')
    df.to_csv(csv_path, index=False)
    print(f"Generated {len(df)} sample tickets and saved to {csv_path}")

    # Display sample distribution
    print("\nTicket Type Distribution:")
    print(df['Ticket Type'].value_counts())


if __name__ == "__main__":
    main()