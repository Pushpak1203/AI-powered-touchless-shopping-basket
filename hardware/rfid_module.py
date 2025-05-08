# rfid_module.py

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def read_rfid():
    """
    Blocks and waits until RFID card is detected.
    Returns: text from RFID tag
    """
    print("Scan your RFID card...")
    try:
        id, text = reader.read()
        return text.strip()
    except Exception as e:
        print("RFID read error:", e)
        return None

def cleanup():
    GPIO.cleanup()
