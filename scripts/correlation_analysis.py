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

    def calculate_correlation(self):
        # Calculate Pearson correlation coefficient
        correlation_results = self.merged_data.groupby('stock_symbol').apply(
            lambda df: pearsonr(df['sentiment'], df['Daily Returns'])[0]
        )
        return correlation_results
    
    def plot_correlation(self, correlation_results):
        # Plot the correlation results
        plt.figure(figsize=(12, 6))
        sns.barplot(x=correlation_results.index, y=correlation_results.values, palette='coolwarm')
        plt.title('Correlation between Sentiment and Stock Returns')
        plt.xlabel('Stock Symbol')
        plt.ylabel('Pearson Correlation Coefficient')
        plt.axhline(0, color='gray', linestyle='--')
        plt.show()

    def scatter_plot(self):
        # Scatter plot of sentiment scores vs. daily stock returns
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='sentiment', y='Daily Returns', hue='stock_symbol', data=self.merged_data, palette='deep')
        plt.title('Sentiment Scores vs. Daily Stock Returns')
        plt.xlabel('Sentiment Scores')
        plt.ylabel('Daily Stock Returns')
        plt.axhline(0, color='gray', linestyle='--')
        plt.axvline(0, color='gray', linestyle='--')
        plt.show()

    def scatter_plot_each(self):
        # Generate a scatter plot for each stock symbol
        stock_symbols = self.merged_data['stock_symbol'].unique()
        
        for symbol in stock_symbols:
            plt.figure(figsize=(12, 6))
            symbol_data = self.merged_data[self.merged_data['stock_symbol'] == symbol]
            sns.scatterplot(x='sentiment', y='Daily Returns', data=symbol_data, palette='deep')
            plt.title(f'Sentiment Scores vs. Daily Stock Returns for {symbol}')
            plt.xlabel('Sentiment Scores')
            plt.ylabel('Daily Stock Returns')
            plt.axhline(0, color='gray', linestyle='--')
            plt.axvline(0, color='gray', linestyle='--')
            plt.show()