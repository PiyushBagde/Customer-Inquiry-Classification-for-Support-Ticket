import os
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).resolve().parents[1])
sys.path.append(project_root)

import pandas as pd
from datetime import datetime
from app import create_app, db
from app.models import Ticket


def init_database():
    app = create_app()
    with app.app_context():
        # Create all tables
        db.create_all()

        # Check if data already exists
        if Ticket.query.first() is None:
            # Create sample data if CSV doesn't exist
            sample_data = [
                [
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-07-19",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Desktop PC",
                        "Date of Purchase": "2024-05-27",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Cannot connect to WiFi",
                        "Ticket Description": "The screen is showing strange colors and flickering frequently."
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-10-05",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Software keeps crashing",
                        "Ticket Description": "The screen is showing strange colors and flickering frequently."
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Wireless Earbuds",
                        "Date of Purchase": "2024-05-22",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Jennifer Martinez",
                        "Customer Email": "jennifer.martinez@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-07-04",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smart Speaker",
                        "Date of Purchase": "2024-10-08",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Emma Wilson",
                        "Customer Email": "emma.wilson@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smart Watch",
                        "Date of Purchase": "2024-11-02",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Wireless Earbuds",
                        "Date of Purchase": "2024-06-16",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Warranty information",
                        "Ticket Description": "Does this model include the new feature announced last month?"
                    },
                    {
                        "Customer Name": "Lisa Anderson",
                        "Customer Email": "lisa.anderson@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-07-02",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Security Camera",
                        "Date of Purchase": "2024-08-12",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Software keeps crashing",
                        "Ticket Description": "My device won't start up after the recent update. I've tried restarting multiple times."
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smart Speaker",
                        "Date of Purchase": "2024-08-22",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Product compatibility question",
                        "Ticket Description": "Does this model include the new feature announced last month?"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Desktop PC",
                        "Date of Purchase": "2024-08-02",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-06-07",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Lisa Anderson",
                        "Customer Email": "lisa.anderson@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-05-27",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Jennifer Martinez",
                        "Customer Email": "jennifer.martinez@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-11-08",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Desktop PC",
                        "Date of Purchase": "2024-08-06",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Jennifer Martinez",
                        "Customer Email": "jennifer.martinez@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-07-16",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Emma Wilson",
                        "Customer Email": "emma.wilson@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Desktop PC",
                        "Date of Purchase": "2024-06-04",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Desktop PC",
                        "Date of Purchase": "2024-06-18",
                        "Ticket Type": "Billing Issue",
                        "Ticket Subject": "Subscription billing error",
                        "Ticket Description": "My subscription is showing the wrong billing amount this month."
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-08-02",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Technical specifications",
                        "Ticket Description": "I need detailed information about the warranty coverage."
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smart Watch",
                        "Date of Purchase": "2024-06-11",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-08-30",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-07-14",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Warranty information",
                        "Ticket Description": "What are the main differences between model A and model B?"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-10-12",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-11-10",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Device not turning on",
                        "Ticket Description": "The application crashes every time I try to open it. This started happening yesterday."
                    },
                    {
                        "Customer Name": "Lisa Anderson",
                        "Customer Email": "lisa.anderson@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-09-20",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Desktop PC",
                        "Date of Purchase": "2024-07-19",
                        "Ticket Type": "Billing Issue",
                        "Ticket Subject": "Double charged for order",
                        "Ticket Description": "My subscription is showing the wrong billing amount this month."
                    },
                    {
                        "Customer Name": "Robert Taylor",
                        "Customer Email": "robert.taylor@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smart Speaker",
                        "Date of Purchase": "2024-10-15",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-10-12",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-08-07",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Battery draining quickly",
                        "Ticket Description": "The screen is showing strange colors and flickering frequently."
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-07-23",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Product comparison",
                        "Ticket Description": "Does this model include the new feature announced last month?"
                    },
                    {
                        "Customer Name": "Robert Taylor",
                        "Customer Email": "robert.taylor@yahoo.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Tablet Elite",
                        "Date of Purchase": "2024-07-28",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Security Camera",
                        "Date of Purchase": "2024-06-25",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-06-11",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Emma Wilson",
                        "Customer Email": "emma.wilson@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Wireless Earbuds",
                        "Date of Purchase": "2024-06-11",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Software keeps crashing",
                        "Ticket Description": "The screen is showing strange colors and flickering frequently."
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Security Camera",
                        "Date of Purchase": "2024-09-29",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Cannot connect to WiFi",
                        "Ticket Description": "Battery life has suddenly decreased, only lasting 2 hours on full charge."
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Security Camera",
                        "Date of Purchase": "2024-11-05",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Robert Taylor",
                        "Customer Email": "robert.taylor@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-08-27",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Emma Wilson",
                        "Customer Email": "emma.wilson@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-05-22",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-09-25",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-11-06",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Emma Wilson",
                        "Customer Email": "emma.wilson@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smart Speaker",
                        "Date of Purchase": "2024-10-09",
                        "Ticket Type": "Billing Issue",
                        "Ticket Subject": "Incorrect price charged",
                        "Ticket Description": "My subscription is showing the wrong billing amount this month."
                    },
                    {
                        "Customer Name": "Jennifer Martinez",
                        "Customer Email": "jennifer.martinez@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-06-04",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Jennifer Martinez",
                        "Customer Email": "jennifer.martinez@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-09-13",
                        "Ticket Type": "Billing Issue",
                        "Ticket Subject": "Incorrect price charged",
                        "Ticket Description": "I returned the item last week but haven't received my refund yet."
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smart Watch",
                        "Date of Purchase": "2024-07-09",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Product comparison",
                        "Ticket Description": "Does this model include the new feature announced last month?"
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@yahoo.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-08-27",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Jennifer Martinez",
                        "Customer Email": "jennifer.martinez@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-09-11",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-10-02",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Feature availability",
                        "Ticket Description": "Could you provide the full technical specifications for this product?"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Desktop PC",
                        "Date of Purchase": "2024-07-26",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Desktop PC",
                        "Date of Purchase": "2024-07-03",
                        "Ticket Type": "Billing Issue",
                        "Ticket Subject": "Double charged for order",
                        "Ticket Description": "I returned the item last week but haven't received my refund yet."
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Tablet Elite",
                        "Date of Purchase": "2024-06-07",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smart Watch",
                        "Date of Purchase": "2024-10-06",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smart Speaker",
                        "Date of Purchase": "2024-07-26",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-06-18",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Michael Brown",
                        "Customer Email": "michael.brown@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Wireless Earbuds",
                        "Date of Purchase": "2024-10-12",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Feature availability",
                        "Ticket Description": "Will this product work with my existing setup? I have a [specific model]."
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Security Camera",
                        "Date of Purchase": "2024-07-18",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-07-15",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Software keeps crashing",
                        "Ticket Description": "The application crashes every time I try to open it. This started happening yesterday."
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smart Watch",
                        "Date of Purchase": "2024-08-06",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-10-06",
                        "Ticket Type": "Billing Issue",
                        "Ticket Subject": "Subscription billing error",
                        "Ticket Description": "There's a charge on my account that I don't recognize."
                    },
                    {
                        "Customer Name": "Emma Wilson",
                        "Customer Email": "emma.wilson@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-10-07",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Wireless Earbuds",
                        "Date of Purchase": "2024-06-28",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-06-11",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Lisa Anderson",
                        "Customer Email": "lisa.anderson@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-09-21",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Robert Taylor",
                        "Customer Email": "robert.taylor@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Tablet Elite",
                        "Date of Purchase": "2024-06-20",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Emma Wilson",
                        "Customer Email": "emma.wilson@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smart Speaker",
                        "Date of Purchase": "2024-07-18",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Lisa Anderson",
                        "Customer Email": "lisa.anderson@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-07-22",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Emma Wilson",
                        "Customer Email": "emma.wilson@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smart Watch",
                        "Date of Purchase": "2024-06-12",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Tablet Elite",
                        "Date of Purchase": "2024-07-07",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Jennifer Martinez",
                        "Customer Email": "jennifer.martinez@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Tablet Elite",
                        "Date of Purchase": "2024-10-07",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Device not turning on",
                        "Ticket Description": "The application crashes every time I try to open it. This started happening yesterday."
                    },
                    {
                        "Customer Name": "Robert Taylor",
                        "Customer Email": "robert.taylor@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smart Watch",
                        "Date of Purchase": "2024-05-30",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-06-04",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-09-10",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-06-07",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@yahoo.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-09-11",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Feature availability",
                        "Ticket Description": "What are the main differences between model A and model B?"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Wireless Earbuds",
                        "Date of Purchase": "2024-07-16",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-11-01",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Tablet Elite",
                        "Date of Purchase": "2024-07-18",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Desktop PC",
                        "Date of Purchase": "2024-07-12",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Michael Brown",
                        "Customer Email": "michael.brown@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-09-17",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-06-04",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Robert Taylor",
                        "Customer Email": "robert.taylor@yahoo.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-10-18",
                        "Ticket Type": "Billing Issue",
                        "Ticket Subject": "Incorrect price charged",
                        "Ticket Description": "There's a charge on my account that I don't recognize."
                    },
                    {
                        "Customer Name": "Robert Taylor",
                        "Customer Email": "robert.taylor@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smartphone X",
                        "Date of Purchase": "2024-10-27",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "James Johnson",
                        "Customer Email": "james.johnson@yahoo.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smart Speaker",
                        "Date of Purchase": "2024-11-05",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Device not turning on",
                        "Ticket Description": "The screen is showing strange colors and flickering frequently."
                    },
                    {
                        "Customer Name": "Lisa Anderson",
                        "Customer Email": "lisa.anderson@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Security Camera",
                        "Date of Purchase": "2024-11-06",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@outlook.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-10-10",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Michael Brown",
                        "Customer Email": "michael.brown@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-10-11",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Robert Taylor",
                        "Customer Email": "robert.taylor@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-10-10",
                        "Ticket Type": "Return Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Laptop Pro",
                        "Date of Purchase": "2024-05-15",
                        "Ticket Type": "Account Access",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@gmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Wireless Earbuds",
                        "Date of Purchase": "2024-10-16",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-10-13",
                        "Ticket Type": "Shipping Problem",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@hotmail.com",
                        "Customer Gender": "Female",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-07-16",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Security Camera",
                        "Date of Purchase": "2024-10-03",
                        "Ticket Type": "Feature Request",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-05-14",
                        "Ticket Type": "Billing Issue",
                        "Ticket Subject": "Subscription billing error",
                        "Ticket Description": "My subscription is showing the wrong billing amount this month."
                    },
                    {
                        "Customer Name": "Maria Garcia",
                        "Customer Email": "maria.garcia@yahoo.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Smart Speaker",
                        "Date of Purchase": "2024-09-27",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@yahoo.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-08-31",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "John Smith",
                        "Customer Email": "john.smith@yahoo.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Security Camera",
                        "Date of Purchase": "2024-09-06",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Device not turning on",
                        "Ticket Description": "Battery life has suddenly decreased, only lasting 2 hours on full charge."
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@hotmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Tablet Elite",
                        "Date of Purchase": "2024-07-12",
                        "Ticket Type": "Product Defect",
                        "Ticket Subject": "General inquiry",
                        "Ticket Description": "General description"
                    },
                    {
                        "Customer Name": "William Thomas",
                        "Customer Email": "william.thomas@outlook.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Fitness Tracker",
                        "Date of Purchase": "2024-11-06",
                        "Ticket Type": "Technical Support",
                        "Ticket Subject": "Cannot connect to WiFi",
                        "Ticket Description": "Unable to connect to any WiFi network. The device doesn't detect any networks."
                    },
                    {
                        "Customer Name": "Lisa Anderson",
                        "Customer Email": "lisa.anderson@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Tablet Elite",
                        "Date of Purchase": "2024-06-10",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Product compatibility question",
                        "Ticket Description": "What are the main differences between model A and model B?"
                    },
                    {
                        "Customer Name": "Sarah Davis",
                        "Customer Email": "sarah.davis@gmail.com",
                        "Customer Gender": "Male",
                        "Product Purchased": "Gaming Console",
                        "Date of Purchase": "2024-09-04",
                        "Ticket Type": "Product Inquiry",
                        "Ticket Subject": "Product comparison",
                        "Ticket Description": "Will this product work with my existing setup? I have a [specific model]."
                    }
                ]
            ]

            # Try to load from CSV if it exists, otherwise use sample data
            try:
                csv_path = os.path.join(project_root, 'data', 'sample_tickets.csv')
                if os.path.exists(csv_path):
                    df = pd.read_csv(csv_path)
                else:
                    df = pd.DataFrame(sample_data)
            except Exception as e:
                print(f"Using default sample data due to error: {e}")
                df = pd.DataFrame(sample_data)

            # Convert data to Ticket objects and add to database
            for _, row in df.iterrows():
                ticket = Ticket(
                    customer_name=row['Customer Name'],
                    customer_email=row['Customer Email'],
                    customer_gender=row['Customer Gender'],
                    product_purchased=row['Product Purchased'],
                    date_of_purchase=datetime.strptime(row['Date of Purchase'], '%Y-%m-%d'),
                    ticket_type=row['Ticket Type'],
                    ticket_subject=row['Ticket Subject'],
                    ticket_description=row['Ticket Description'],
                    status='unresolved'
                )
                db.session.add(ticket)

            db.session.commit()
            print("Database initialized with sample data!")
        else:
            print("Database already contains data!")


if __name__ == '__main__':
    init_database()