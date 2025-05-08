from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Firebase Imports
import os
import firebase_admin
from firebase_admin import credentials, db as firebase_db

# Initialize database (MySQL via SQLAlchemy)
db = SQLAlchemy()

# ============ Firebase Setup ============
firebase_config_path = os.getenv("FIREBASE_CONFIG_PATH")
firebase_db_url = os.getenv("FIREBASE_DATABASE_URL")

if firebase_config_path and firebase_db_url:
    try:
        cred = credentials.Certificate(firebase_config_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': firebase_db_url
        })
        print("✅ Firebase initialized successfully")
    except Exception as e:
        print(f"⚠️ Firebase initialization error: {e}")
# ========================================


# ===================== SQLAlchemy Models =====================

# User Model (Authentication via RFID & Voice)
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    rfid_tag = db.Column(db.String(50), unique=True, nullable=False)  # RFID for authentication
    voice_profile = db.Column(db.LargeBinary, nullable=True)  # Optional voice profile for future use
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    cart_items = db.relationship('Cart', back_populates='user', cascade='all, delete-orphan')
    transactions = db.relationship('Transaction', back_populates='user', cascade='all, delete-orphan')


# Product Model (Product Details)
class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)  # Optional image link
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    cart_products = db.relationship('Cart', back_populates='product', cascade='all, delete-orphan')


# Cart Model (Items in the Shopping Basket)
class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', back_populates='cart_items')
    product = db.relationship('Product', back_populates='cart_products')


# Transactions Model (Billing & Payment)
class Transaction(db.Model):
    __tablename__ = 'transactions'
    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(20), default="Pending")  # Pending, Completed, Failed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    user = db.relationship('User', back_populates='transactions')
