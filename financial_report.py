# financial_report.py
from utils.finance_api import FinanceAPI
from utils.excel_report import ExcelReportGenerator

# Main execution
if __name__ == '__main__':
    # Define the stock symbol, start date, and end date for fetching data
    stock_symbol = 'AAPL'  # Apple stock symbol
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    
    # Step 1: Fetch the financial data
    api = FinanceAPI(stock_symbol, start_date, end_date)
    stock_data = api.fetch_data()

    # If data is fetched successfully, proceed to generate the report
    if not stock_data.empty:
        # Step 2: Generate the Excel report
        report_generator = ExcelReportGenerator(stock_data, 'financial_report.xlsx')
        report_generator.generate_excel_report()