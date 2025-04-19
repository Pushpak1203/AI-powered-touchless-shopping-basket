# backend/utils.py

import datetime

def format_datetime(dt=None):
    dt = dt or datetime.datetime.utcnow()
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def log_event(message):
    print(f"[{format_datetime()}] {message}")
