import unittest
from models.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "Widget", 19.99, "Gadgets", 100)

    def test_product_initialization(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, "Widget")
        self.assertEqual(self.product.price, 19.99)
        self.assertEqual(self.product.category, "Gadgets")
        self.assertEqual(self.product.quantity, 100)

    def test_product_str(self):
        self.assertEqual(str(self.product), "Product 1: Widget, Price: 19.99, Category: Gadgets, Quantity: 100")

    def test_product_to_dict(self):
        expected_dict = {
            "product_id": 1,
            "name": "Widget",
            "price": 19.99,
            "quantity": 100,
            "category": "Gadgets"
        }
        self.assertEqual(self.product.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()
