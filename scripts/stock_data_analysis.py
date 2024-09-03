import pandas as pd
import matplotlib.pyplot as plt
import talib
import pynance as pn
import glob
import os

class stockeda:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    def load_data(self):
        # Load all CSV files
        all_files = glob.glob(os.path.join(self.folder_path, "*.csv"))
        
        # Init an empty list to hold dataframes
        df_list = []
        
        for file in all_files:
            # Extract the stock symbol from the file name
            filename = os.path.basename(file)
            stock_symbol = filename.split('_')[0]
            df = pd.read_csv(file) # Read the CSV file into a dataframe
            df['stock_symbol'] = stock_symbol  # Add the stock_symbol column to the dataframe
            df_list.append(df) # Append the dataframe to the list
   
        self.data = pd.concat(df_list, ignore_index=True)   # Concatenate all dataframes
        self.data['Date'] = pd.to_datetime(self.data['Date']) # Convert the 'Date' column to datetime
        
        return self.data  # return the expected data
    
    def data_descriptive(self):
        # Check for missing values
        missing_values = self.data.isnull().sum()
        print("Missing values:")
        print(missing_values)

        # Check for duplicates
        duplicates = self.data.duplicated().sum()
        print("\n\n Number of duplicates:", duplicates)

        # Check data types
        data_types = self.data.dtypes
        print("\n\n Data types:")
        print(data_types)

        # Descriptive statistics
        descriptive_stats = self.data.describe(include='all')
        print("\n\n Descriptive Statistics:")
        print(descriptive_stats)


    def calc_tech_ind(self, df):
        # Ensure data is sorted by Date
        df = df.sort_values(['Date'])
        
        # Calculate technical indicators
        df['SMA'] = talib.SMA(df['Close'], timeperiod=20)
        df['EMA'] = talib.EMA(df['Close'], timeperiod=20)
        df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
        df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'])
        
        return df


    def apply_ta_ind(self):
        # Apply technical indicators for each stock symbol
        df_dict = {}
        for symbol in self.data['stock_symbol'].unique():
            df = self.data[self.data['stock_symbol'] == symbol].copy()
            df = self.calc_tech_ind(df)
            df_dict[symbol] = df
        
        self.data_with_indicators = pd.concat(df_dict.values(), ignore_index=True)
        return self.data_with_indicators

    def vis_stocks(self, df):
        # Plot technical indicators for each stock symbol
        for symbol in df['stock_symbol'].unique():
            stock_df = df[df['stock_symbol'] == symbol]
            
            plt.figure(figsize=(14, 7))
            plt.plot(stock_df['Date'], stock_df['Close'], label='Close Price', color='black')
            plt.plot(stock_df['Date'], stock_df['SMA'], label='SMA', color='blue')
            plt.plot(stock_df['Date'], stock_df['EMA'], label='EMA', color='red')
            plt.title(f'{symbol} Price with SMA and EMA')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.grid(True)
            plt.show()

    def cal_fin_metrics(self):
        # Ensure data is sorted by Date for consistency
        self.data_with_indicators = self.data_with_indicators.sort_values(['stock_symbol', 'Date'])
        
        # Calculate financial metrics for each stock symbol
        metrics_dict = {}
        for symbol in self.data_with_indicators['stock_symbol'].unique():
            df = self.data_with_indicators[self.data_with_indicators['stock_symbol'] == symbol].copy()
            
            # Calculate daily returns using Pandas
            df['Daily Returns'] = df['Close'].pct_change()
            
            # Calculate additional metrics
            df['Rolling Volatility'] = df['Daily Returns'].rolling(window=20).std()
            df['Moving Average'] = df['Close'].rolling(window=20).mean()
            df['Cumulative Returns'] = (1 + df['Daily Returns']).cumprod() - 1
            
            metrics_dict[symbol] = df
        
        self.data_with_financial_metrics = pd.concat(metrics_dict.values(), ignore_index=True)
        return self.data_with_financial_metrics


    def plot_fin_metrics(self):
        # Plot financial metrics for each stock symbol
        for symbol in self.data_with_financial_metrics['stock_symbol'].unique():
            stock_df = self.data_with_financial_metrics[self.data_with_financial_metrics['stock_symbol'] == symbol]
            
            plt.figure(figsize=(14, 7))
            plt.plot(stock_df['Date'], stock_df['Daily Returns'], label='Daily Returns', color='green')
            plt.plot(stock_df['Date'], stock_df['Rolling Volatility'], label='Rolling Volatility', color='orange')
            plt.plot(stock_df['Date'], stock_df['Cumulative Returns'], label='Cumulative Returns', color='purple')
            plt.title(f'{symbol} Financial Metrics')
            plt.xlabel('Date')
            plt.ylabel('Value')
            plt.legend()
            plt.grid(True)
            plt.show()

    def save_to_csv(self, output_path="../data/processed_stock_data.csv"):
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        # Save the dataframe to a CSV file
        self.data.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")
