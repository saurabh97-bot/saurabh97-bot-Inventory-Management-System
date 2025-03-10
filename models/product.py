# product.py

class Product:
    def __init__(self, id, name, price, category, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    def __str__(self):
        return f"Product {self.id}: {self.name}, Price: {self.price}, Category: {self.category}, Quantity: {self.quantity}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category
        }
