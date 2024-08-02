from models.transaction import Transaction
from datetime import datetime

class Return(Transaction):
    def __init__(self, id, product_id, quantity, reason):
        super().__init__(id, product_id, quantity, 0) 
        self.reason = reason
        self.date = datetime.now()

    def __str__(self):
        return f"Return {self.id}: Product {self.product_id}, Quantity: {self.quantity}, Reason: {self.reason}, Date: {self.date}"

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "reason": self.reason,
            "date": self.date
        }