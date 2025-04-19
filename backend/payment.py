# backend/payment.py

import razorpay
from flask import current_app
from models import db, Transaction

def initiate_payment(user_id, amount):
    client = razorpay.Client(
        auth=(current_app.config['RAZORPAY_KEY_ID'], current_app.config['RAZORPAY_SECRET'])
    )
    
    payment = client.order.create({
        "amount": int(amount * 100),  # Convert to paise
        "currency": "INR",
        "receipt": f"receipt_user_{user_id}",
        "payment_capture": 1
    })

    # Log transaction to DB
    transaction = Transaction(
        user_id=user_id,
        total_amount=amount,
        payment_status="Pending"
    )
    db.session.add(transaction)
    db.session.commit()

    return {
        "order_id": payment["id"],
        "currency": payment["currency"],
        "amount": payment["amount"],
        "status": "created"
    }
