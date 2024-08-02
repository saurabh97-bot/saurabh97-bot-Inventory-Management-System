from models.transaction import Transaction
from datetime import datetime

class Sale(Transaction):
    sales = []

    def __init__(self, id, product_id, quantity, price):
        super().__init__(id, product_id, quantity, price)
        self.date = datetime.now()
        Sale.sales.append(self)

    @staticmethod
    def get_all_sales():
        return Sale.sales

    def __str__(self):
        return f"Sale {self.id}: Product {self.product_id}, Quantity: {self.quantity}, Price: {self.price}, Date: {self.date}"

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "price": self.price,
            "date": self.date
        }