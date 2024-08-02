from models.product import Product
from models.sale import Sale
from models._return import Return

class Inventory:
    def __init__(self):
        self.products = {}
        self.sales = []
        self.returns = []

    def add_product(self, product):
        self.products[product.id] = product

    def update_product(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity = quantity
        else:
            print("Product not found.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

    def view_products(self):
        for product in self.products.values():
            print(product)

    def get_product(self, product_id):
        return self.products.get(product_id)

    def record_sale(self, product_id, quantity, price):
        product = self.get_product(product_id)
        if product:
            if product.quantity >= quantity:
                sale = Sale(len(self.sales) + 1, product_id, quantity, price)
                product.quantity -= quantity
                self.sales.append(sale)
                return sale
            else:
                print("Not enough quantity in stock.")
        else:
            print("Product not found.")

    def record_return(self, product_id, quantity, reason):
        product = self.get_product(product_id)
        if product:
            return_obj = Return(len(self.returns) + 1, product_id, quantity, reason)
            product.quantity += quantity
            self.returns.append(return_obj)
            return return_obj
        else:
            print("Product not found.")

    def view_sales(self):
        for sale in self.sales:
            print(sale)

    def view_returns(self):
        for return_obj in self.returns:
            print(return_obj)