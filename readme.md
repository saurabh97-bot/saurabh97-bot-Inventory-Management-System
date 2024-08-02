# Advanced Inventory Management System with Invoicing


## Overview

This project is an **Advanced Inventory Management System** that includes features for managing inventory, tracking sales and returns, and generating invoices. The system is built using Python and includes both class-based structures and a command-line interface (CLI) for interaction.

## Features

- **Product Management:** Add, update, and manage products in the inventory.
- **Sales Tracking:** Record and track sales transactions.
- **Returns Management:** Handle and record product returns.
- **Invoice Generation:** Generate PDF invoices for individual products based on sales data.
- **Reporting:** Generate CSV reports summarizing sales data.

## Project Structure

Inventory-System/
│
├── models/
│ ├── product.py
│ ├── inventory.py
│ ├── sale.py
│ ├── _return.py
│ └── invoice.py
│
├── scripts/
│ ├── generate_reports.py
| └── cli.py
│
├── tests/
│ ├── test_product.py
│ ├── test_inventory.py
│ ├── test_sale.py
│ ├── test_return.py
│ ├── test_invoice.py
│ └── test_report.py
│
├── reports/
│ ├── invoices/ # Generated invoices
│ └── csv_reports/ # Generated CSV reports
│
├── brief_report.docx
├── main.py
├── requirements.txt
└── README.md

## Installation

1. **Clone the Repository:**

   * git clone https://github.com/saurabh97-bot/Inventory-Management-System.git
   * cd Inventory-Management-System

2. **Install Dependencies**

   * pip install -r requirements.txt
  
## Usage

1. **Run the Application:** Use the main.py file to run the application. This will set up the inventory, record sales and returns, generate invoices, and create reports.

   * python main.py
  
2. **Generate Invoices:** You can generate individual invoices by calling the Invoice class with a specific product_id using the CLI.

3. **View Reports:** Generated invoices and reports will be saved in the reports/invoices/ and reports/csv_reports/ directories, respectively.


## Challenges Faced

* **Integration of Different Components:** Ensuring seamless interaction between product management, sales tracking, returns handling, and invoice generation.
* **Invoice Customization:** Customizing invoices to include specific product details while ensuring PDF generation works across various environments.
* **Data Integrity:** Ensuring that sales and returns data accurately reflect inventory changes and are consistently recorded.

## Conclusion

This project provides a comprehensive system for managing inventory and sales in a business environment. Future enhancements could include a graphical user interface (GUI) or web-based interface to improve user interaction and extend functionality.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

