import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

class Corr_analysis:
    def __init__(self, financial_data_path, stock_data_path):
        self.financial_data_path = financial_data_path
        self.stock_data_path = stock_data_path

    def load_data(self):
        self.financial_data = pd.read_csv(self.financial_data_path)
        self.stock_data = pd.read_csv(self.stock_data_path)
        return self.financial_data, self.stock_data

    def prepare_data(self):
        # Convert date columns to datetime format
        self.financial_data['date'] = pd.to_datetime(self.financial_data['date'])
        self.stock_data['Date'] = pd.to_datetime(self.stock_data['Date'])
        
        # Align dates and normalize date formats
        self.financial_data['publication_date'] = self.financial_data['date'].dt.date
        self.stock_data['Date'] = self.stock_data['Date'].dt.date

        # Group by date and calculate average sentiment per day
        daily_sentiment = self.financial_data.groupby(['publication_date', 'stock'])['sentiment'].mean().reset_index()
        
        # Calculate daily stock returns
        self.stock_data['Daily Returns'] = self.stock_data.groupby('stock_symbol')['Adj Close'].pct_change()
        
        # Merge financial data with stock data on date and stock symbol
        self.merged_data = pd.merge(daily_sentiment, 
                                    self.stock_data, 
                                    left_on=['publication_date', 'stock'], 
                                    right_on=['Date', 'stock_symbol'], 
                                    how='inner')

        return self.merged_data

    
