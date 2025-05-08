# sensors_config.py

import time
import RPi.GPIO as GPIO

# GPIO setup
TRIG_PIN = 23
ECHO_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def read_distance():
    """
    Measure distance using HC-SR04 Ultrasonic Sensor
    Returns: distance in cm
    """
    # Send pulse
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.1)
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Wait for echo
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # cm
    distance = round(distance, 2)
    return distance

def cleanup():
    GPIO.cleanup()
