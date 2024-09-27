# utils/finance_api.py
import yfinance as yf

class FinanceAPI:
    """
    This class handles fetching financial data from the Yahoo Finance API.
    """

    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    def fetch_data(self):
        """
        Fetches historical stock data for the specified symbol and date range.
        Returns a Pandas DataFrame containing the stock data.
        """
        print(f"Fetching data for {self.symbol} from {self.start_date} to {self.end_date}...")
        stock_data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        
        if stock_data.empty:
            print("No data was found for the specified symbol and date range.")
        else:
            print(f"Data successfully fetched. {len(stock_data)} entries found.")
        
        return stock_data