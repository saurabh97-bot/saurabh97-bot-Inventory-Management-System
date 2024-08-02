import csv
from models.sale import Sale

class ReportGenerator:
    def __init__(self, file_path='reports/csv_reports/sales_report.csv'):
        self.file_path = file_path

    def generate_report(self):
        sales = Sale.get_all_sales()
        try:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Sale ID", "Product ID", "Quantity", "Price", "Date"])
                for sale in sales:
                    writer.writerow([
                        sale.id,
                        sale.product_id,
                        sale.quantity,
                        sale.price,
                        sale.date.strftime('%Y-%m-%d %H:%M:%S')  # Format date
                    ])
            print(f"Report generated: {self.file_path}")
        except IOError as e:
            print(f"Error generating report: {e}")

# Example usage:
# report_generator = ReportGenerator()
# report_generator.generate_report()
