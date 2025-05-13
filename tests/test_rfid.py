# tests/test_rfid.py

import sys
import os
import pytest
from flask import Flask

# Dynamically add backend folder to import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from authentication import authenticate_user
from models import db, User
from config import Config

# Setup Flask app context for DB access
@pytest.fixture(scope="module")
def test_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use in-memory DB for testing
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app

def test_rfid_authentication(test_app):
    with test_app.app_context():
        # Add mock user
        test_user = User(name="Test User", email="test@example.com", rfid_tag="RFID123")
        db.session.add(test_user)
        db.session.commit()

        # Test valid RFID
        result = authenticate_user("RFID123")
        assert result.name == "Test User"

        # Test invalid RFID
        result = authenticate_user("INVALID_RFID")
        assert result is None
