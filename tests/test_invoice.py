# tests/test_invoice.py
import unittest
from models.invoice import Invoice
from models.sale import Sale
from models.product import Product
import os

class TestInvoice(unittest.TestCase):

    def setUp(self):
        self.product1 = Product(id=1, name="Widget", price=19.99, category="Gadgets", quantity=100)
        self.product2 = Product(id=2, name="Gizmo", price=29.99, category="Gadgets", quantity=50)

        Sale(id=1, product_id=1, quantity=5, price=19.99)
        Sale(id=2, product_id=1, quantity=2, price=19.99)
        Sale(id=3, product_id=2, quantity=1, price=29.99)

    def test_generate_invoice(self):
        invoice1 = Invoice(product_id=1)
        invoice1.generate_invoice()

        invoice2 = Invoice(product_id=2)
        invoice2.generate_invoice()

        # Check if files are generated
        self.assertTrue(os.path.exists('reports/invoices/invoice_product_1.pdf'))
        self.assertTrue(os.path.exists('reports/invoices/invoice_product_2.pdf'))

if __name__ == '__main__':
    unittest.main()
