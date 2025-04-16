import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask Configuration
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

    # Database Configuration (MySQL)
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Firebase Configuration (If using Firebase)
    FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
    FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL")

    # Razorpay Payment API Keys
    RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
    RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")
