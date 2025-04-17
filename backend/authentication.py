from models import User
from flask import current_app

def authenticate_user(rfid_tag):
    """
    Authenticate a user based on their RFID tag.
    Returns the user object if found, otherwise None.
    """
    try:
        # Query the user from the database using the RFID tag
        user = User.query.filter_by(rfid_tag=rfid_tag).first()
        if user:
            current_app.logger.info(f"User authenticated: {user.name}")
        else:
            current_app.logger.warning(f"RFID not recognized: {rfid_tag}")
        return user
    except Exception as e:
        current_app.logger.error(f"Error during RFID authentication: {str(e)}")
        return None
