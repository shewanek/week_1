import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class FinancialNewsEDA:
    def __init__(self, file_path):
        self.file_path = file_path
    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        return self.data

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



