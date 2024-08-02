import unittest
from models.sale import Sale

class TestSale(unittest.TestCase):
    def setUp(self):
        self.sale = Sale(1, 1, 5, 19.99)

    def test_sale_initialization(self):
        self.assertEqual(self.sale.id, 1)
        self.assertEqual(self.sale.product_id, 1)
        self.assertEqual(self.sale.quantity, 5)
        self.assertEqual(self.sale.price, 19.99)

    def test_sale_str(self):
        expected_str = f"Sale 1: Product 1, Quantity: 5, Price: 19.99, Date: {self.sale.date.strftime('%Y-%m-%d %H:%M:%S')}"
        self.assertEqual(str(self.sale), expected_str)

    def test_sale_to_dict(self):
        expected_dict = {
            "id": 1,
            "product_id": 1,
            "quantity": 5,
            "price": 19.99,
            "date": self.sale.date.strftime('%Y-%m-%d %H:%M:%S')
        }
        self.assertEqual(self.sale.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()
