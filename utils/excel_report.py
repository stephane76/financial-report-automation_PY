# utils/excel_report.py
# utils/excel_report.py
import pandas as pd

class ExcelReportGenerator:
    """
    This class handles generating an Excel report from the financial data.
    """

    def __init__(self, data, output_file):
        self.data = data
        self.output_file = output_file

    def process_data(self):
        """
        Resamples the data to calculate the monthly average closing price and total volume.
        """
        # Resample the data by month and calculate average close price and total volume
        monthly_data = self.data.resample('M').agg({
            'Close': 'mean',
            'Volume': 'sum'
        })
        monthly_data.columns = ['Average Close Price', 'Total Volume']

        # Round the average close price to 2 decimal places for readability
        monthly_data['Average Close Price'] = monthly_data['Average Close Price'].round(2)

        # Format the dates (index) to show only year and month
        monthly_data.index = monthly_data.index.strftime('%Y-%m')

        return monthly_data

    def generate_excel_report(self):
        """
        Generates an Excel report from the processed financial data.
        """
        processed_data = self.process_data()

        # Save the processed data to an Excel file
        processed_data.to_excel(self.output_file, engine='openpyxl')

        print(f"Excel report generated: {self.output_file}")