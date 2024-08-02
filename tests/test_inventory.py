import unittest
from models.inventory import Inventory
from models.product import Product
from models.sale import Sale
from models._return import Return

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.product = Product(1, "Widget", 19.99, "Gadgets", 100)
        self.inventory.add_product(self.product)

    def test_add_product(self):
        self.assertEqual(self.inventory.get_product(1), self.product)

    def test_update_product(self):
        self.inventory.update_product(1, 150)
        self.assertEqual(self.inventory.get_product(1).quantity, 150)

    def test_remove_product(self):
        self.inventory.remove_product(1)
        self.assertIsNone(self.inventory.get_product(1))

    def test_record_sale(self):
        sale = self.inventory.record_sale(1, 5, 19.99)
        self.assertEqual(sale.product_id, 1)
        self.assertEqual(sale.quantity, 5)
        self.assertEqual(sale.price, 19.99)
        self.assertEqual(self.inventory.get_product(1).quantity, 95)

    def test_record_return(self):
        self.inventory.record_sale(1, 5, 19.99)
        return_obj = self.inventory.record_return(1, 3, "Defective")
        self.assertEqual(return_obj.reason, "Defective")
        self.assertEqual(self.inventory.get_product(1).quantity, 98)

if __name__ == "__main__":
    unittest.main()
