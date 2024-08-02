# sale_system.py

from models.product import Product
from models.sale import Sale
from models.invoice import Invoice

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    product = Product(name, price)
    print(f"Product {product.name} added with price ${product.price:.2f}")

def record_sale():
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    sale = Sale(product_id, quantity)
    print(f"Sale recorded for product {sale.product_id} with quantity {sale.quantity}")

def create_invoice():
    sale_id = int(input("Enter sale ID: "))
    invoice = Invoice(sale_id)
    print(f"Invoice created for sale {sale_id}")

def display_products():
    products = Product.get_all_products()
    for product in products:
        print(product)

def display_sales():
    sales = Sale.get_all_sales()
    for sale in sales:
        print(sale)

def display_invoices():
    invoices = Invoice.get_all_invoices()
    for invoice in invoices:
        print(invoice)

def main():
    while True:
        print("Sale System CLI")
        print("1. Add product")
        print("2. Record sale")
        print("3. Create invoice")
        print("4. Display products")
        print("5. Display sales")
        print("6. Display invoices")
        print("7. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            record_sale()
        elif choice == "3":
            create_invoice()
        elif choice == "4":
            display_products()
        elif choice == "5":
            display_sales()
        elif choice == "6":
            display_invoices()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()