import argparse
from models.product import Product
from models.inventory import Inventory
from models.sale import Sale
from models._return import Return
from models.invoice import Invoice
from generate_reports import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Inventory Management System")
    subparsers = parser.add_subparsers(dest='command')

    # Add product
    add_product_parser = subparsers.add_parser('add_product', help='Add a new product')
    add_product_parser.add_argument('id', type=int, help='Product ID')
    add_product_parser.add_argument('name', type=str, help='Product Name')
    add_product_parser.add_argument('price', type=float, help='Product Price')
    add_product_parser.add_argument('category', type=str, help='Product Category')
    add_product_parser.add_argument('quantity', type=int, help='Product Quantity')

    # Record sale
    record_sale_parser = subparsers.add_parser('record_sale', help='Record a new sale')
    record_sale_parser.add_argument('product_id', type=int, help='Product ID')
    record_sale_parser.add_argument('quantity', type=int, help='Quantity Sold')
    record_sale_parser.add_argument('price', type=float, help='Sale Price')

    # Record return
    record_return_parser = subparsers.add_parser('record_return', help='Record a return')
    record_return_parser.add_argument('product_id', type=int, help='Product ID')
    record_return_parser.add_argument('quantity', type=int, help='Quantity Returned')
    record_return_parser.add_argument('reason', type=str, help='Return Reason')

    # Generate report
    generate_report_parser = subparsers.add_parser('generate_report', help='Generate sales report')

    args = parser.parse_args()

    if args.command == 'add_product':
        product = Product(args.id, args.name, args.price, args.category, args.quantity)
        inventory = Inventory()
        inventory.add_product(product)
        print("Product added.")
    
    elif args.command == 'record_sale':
        sale = Sale(len(Sale.get_all_sales()) + 1, args.product_id, args.quantity, args.price)
        inventory = Inventory()
        inventory.record_sale(args.product_id, args.quantity, args.price)
        print("Sale recorded.")
    
    elif args.command == 'record_return':
        return_obj = Return(len(Return.get_all_returns()) + 1, args.product_id, args.quantity, args.reason)
        inventory = Inventory()
        inventory.record_return(args.product_id, args.quantity, args.reason)
        print("Return recorded.")
    
    elif args.command == 'generate_report':
        report_generator = ReportGenerator()
        report_generator.generate_report()
        print("Report generated.")

if __name__ == "__main__":
    main()
