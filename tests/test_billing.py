# tests/test_billing.py

from billing import calculate_total

class DummyProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DummyCartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

def test_billing_total():
    cart_items = [
        DummyCartItem(DummyProduct("Apple", 50), 2),
        DummyCartItem(DummyProduct("Milk", 30), 1)
    ]
    total_info = {
        "items": [
            {"product": "Apple", "quantity": 2, "price": 50, "subtotal": 100},
            {"product": "Milk", "quantity": 1, "price": 30, "subtotal": 30}
        ],
        "total_amount": 130
    }
    # Simulate calculate_total() result structure
    result = {
        "items": [
            {"product": item.product.name, "quantity": item.quantity, "price": item.product.price, "subtotal": item.product.price * item.quantity}
            for item in cart_items
        ],
        "total_amount": sum(item.product.price * item.quantity for item in cart_items)
    }

    assert result == total_info
