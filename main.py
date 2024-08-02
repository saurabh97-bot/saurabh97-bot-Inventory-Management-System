from models.product import Product
from models.inventory import Inventory
from models.sale import Sale
from models._return import Return
from models.invoice import Invoice
from scripts.generate_reports import ReportGenerator

# Setup Inventory and Products
def setup_inventory():
    # Create an Inventory instance
    inventory = Inventory()

    # Add some products
    product1 = Product(id=1, name="Widget", price=19.99, category="Gadgets", quantity=100)
    product2 = Product(id=2, name="Gizmo", price=29.99, category="Gadgets", quantity=50)

    inventory.add_product(product1)
    inventory.add_product(product2)
    return inventory

# Record Sales and Returns
def record_sales_returns():
    # Record some sales
    sale1 = Sale(id=1, product_id=1, quantity=5, price=19.99)
    sale2 = Sale(id=2, product_id=2, quantity=2, price=29.99)

    # Record some returns
    return1 = Return(id=1, product_id=1, quantity=3, reason="Defective")

def generate_invoice(inventory):
    # Generate an invoice
    product_ids = [1, 2]  # List of product IDs for which to generate invoices
    for product_id in product_ids:
        invoice = Invoice(product_id, inventory)
        invoice.generate_invoice()

def check_csv_report():
    # Generate a report
    report_generator = ReportGenerator()
    report_generator.generate_report()

# Execute all functions
def run_all():
    # Setup inventory
    inventory = setup_inventory()

    # Record sales and returns
    record_sales_returns()

    # Generate invoices for all products
    generate_invoice(inventory)

    # Check CSV report
    check_csv_report()

    print("All operations completed successfully.")

if __name__ == "__main__":
    run_all()
