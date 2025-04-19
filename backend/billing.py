# backend/billing.py

from models import db, Cart, Product

def calculate_total(user_id):
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    total = 0
    item_list = []

    for item in cart_items:
        price = item.product.price
        subtotal = price * item.quantity
        item_list.append({
            "product": item.product.name,
            "quantity": item.quantity,
            "price": price,
            "subtotal": subtotal
        })
        total += subtotal

    return {
        "items": item_list,
        "total_amount": total
    }
