from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize database
db = SQLAlchemy()

# User Model (Authentication via RFID & Voice)
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    rfid_tag = db.Column(db.String(50), unique=True, nullable=False)  # RFID for authentication
    voice_profile = db.Column(db.LargeBinary, nullable=True)  # Store voice profile (optional)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Product Model (Product Details)
class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)  # Store product image URL
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Cart Model (Items in the Shopping Basket)
class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', backref=db.backref('cart_items', lazy=True))
    product = db.relationship('Product', backref=db.backref('cart_products', lazy=True))

# Transactions Model (Billing & Payment)
class Transaction(db.Model):
    __tablename__ = 'transactions'
    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(20), default="Pending")  # Status: Pending, Completed, Failed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    user = db.relationship('User', backref=db.backref('transactions', lazy=True))
