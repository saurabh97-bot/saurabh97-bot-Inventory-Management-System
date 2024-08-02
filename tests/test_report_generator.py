import unittest
from scripts.generate_reports import ReportGenerator
from models.sale import Sale
import os

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.report_generator = ReportGenerator()
        Sale.sales.clear()  # Ensure no residual sales data
        Sale(1, 1, 5, 19.99)
        self.report_file = 'reports/csv_reports/sales_report.csv'

    def test_generate_report(self):
        self.report_generator.generate_report()
        self.assertTrue(os.path.exists(self.report_file))
        with open(self.report_file, 'r') as file:
            lines = file.readlines()
        self.assertGreater(len(lines), 1)  # Check that file is not empty

if __name__ == "__main__":
    unittest.main()
