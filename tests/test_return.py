import unittest
from models._return import Return

class TestReturn(unittest.TestCase):
    def setUp(self):
        self.return_obj = Return(1, 1, 3, "Defective")

    def test_return_initialization(self):
        self.assertEqual(self.return_obj.id, 1)
        self.assertEqual(self.return_obj.product_id, 1)
        self.assertEqual(self.return_obj.quantity, 3)
        self.assertEqual(self.return_obj.reason, "Defective")

    def test_return_str(self):
        expected_str = f"Return 1: Product 1, Quantity: 3, Reason: Defective, Date: {self.return_obj.date.strftime('%Y-%m-%d %H:%M:%S')}"
        self.assertEqual(str(self.return_obj), expected_str)

    def test_return_to_dict(self):
        expected_dict = {
            "id": 1,
            "product_id": 1,
            "quantity": 3,
            "reason": "Defective",
            "date": self.return_obj.date.strftime('%Y-%m-%d %H:%M:%S')
        }
        self.assertEqual(self.return_obj.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()
