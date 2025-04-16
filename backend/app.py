from flask import Flask, jsonify
from models import db
from config import Config
from authentication import authenticate_user

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Create tables within app context
    with app.app_context():
        db.create_all()

    # Define routes
    @app.route('/')
    def home():
        return "AI-Powered Touchless Shopping Basket API is running!"

    # Test RFID Authentication (Temporary API)
    @app.route('/scan-rfid/<rfid_tag>')
    def scan_rfid(rfid_tag):
        user = authenticate_user(rfid_tag)
        if user:
            return jsonify({"message": f"User {user.name} authenticated successfully!"})
        else:
            return jsonify({"error": "RFID not recognized"}), 401

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
