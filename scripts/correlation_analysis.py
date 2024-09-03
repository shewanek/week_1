import pandas as pd


class Corr_analysis:
    def __init__(self, financial_data_path, stock_data_path):
        self.financial_data_path = financial_data_path
        self.stock_data_path = stock_data_path

    def load_data(self):
        self.financial_data = pd.read_csv(self.financial_data_path)
        self.stock_data = pd.read_csv(self.stock_data_path)
        return self.financial_data, self.stock_data

    