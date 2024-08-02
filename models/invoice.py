import os
from fpdf import FPDF
from models.sale import Sale
from models.product import Product
from models.inventory import Inventory  # Import Inventory class

class Invoice:
    def __init__(self, product_id, inventory):
        self.product_id = product_id
        self.inventory = inventory  # Add inventory to the constructor

    def generate_invoice(self):
        # Fetch sales for the given product ID
        sales = [sale for sale in Sale.get_all_sales() if sale.product_id == self.product_id]
        if not sales:
            print(f"No sales found for Product ID {self.product_id}")
            return

        # Get product details from inventory
        product = self.inventory.get_product(self.product_id)
        if not product:
            print(f"Product ID {self.product_id} not found in inventory.")
            return

        # Create directory for invoice reports
        dir_path = "reports/invoices/"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Generate the invoice PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)

        pdf.cell(200, 10, txt=f"Invoice for Product {product.name}", ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        pdf.cell(100, 10, txt=f"Date: {sales[0].date.strftime('%Y-%m-%d')}", ln=True)
        pdf.ln(10)

        pdf.set_font("Arial", size=10)
        pdf.cell(50, 10, txt="Sale ID", border=1)
        pdf.cell(50, 10, txt="Quantity", border=1)
        pdf.cell(50, 10, txt="Price", border=1)
        pdf.cell(50, 10, txt="Total", border=1, ln=True)

        total = 0
        for sale in sales:
            pdf.cell(50, 10, txt=str(sale.id), border=1)
            pdf.cell(50, 10, txt=str(sale.quantity), border=1)
            pdf.cell(50, 10, txt="${:.2f}".format(sale.price), border=1)
            pdf.cell(50, 10, txt="${:.2f}".format(sale.quantity * sale.price), border=1, ln=True)
            total += sale.quantity * sale.price

        pdf.ln(10)
        pdf.cell(150, 10, txt="Subtotal:", border=1)
        pdf.cell(50, 10, txt="${:.2f}".format(total), border=1, ln=True)

        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt="Thank you for your purchase!", ln=True, align='C')

        filename = f"invoice_product_{self.product_id}.pdf"
        file_path = os.path.join(dir_path, filename)
        try:
            pdf.output(file_path, "F")
            print(f"Invoice generated: {file_path}")
        except Exception as e:
            print(f"Error generating PDF file: {e}")

    def get_product_details(self, product_id):
        # Fetch product from the inventory
        return self.inventory.get_product(product_id)
