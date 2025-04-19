# backend/navigation.py

import random
from datetime import datetime

# Simulated store sections
STORE_SECTIONS = [
    "Fruits & Vegetables",
    "Dairy",
    "Bakery",
    "Snacks & Beverages",
    "Frozen Foods",
    "Meat & Seafood",
    "Personal Care",
    "Household Items",
    "Electronics",
    "Checkout"
]

# Store simulated user positions here
user_positions = {}

def get_current_section():
    """
    Randomly simulate which section the user/cart is currently in.
    Replace this with actual sensor-based location tracking in real prototype.
    """
    return random.choice(STORE_SECTIONS)

def update_user_location(user_id):
    """
    Update and return the user's current location with timestamp.
    """
    section = get_current_section()
    timestamp = datetime.utcnow()
    user_positions[user_id] = {
        "section": section,
        "timestamp": timestamp
    }
    return user_positions[user_id]

def get_user_location(user_id):
    """
    Get the last known location of a user.
    """
    return user_positions.get(user_id, {
        "section": "Unknown",
        "timestamp": None
    })
