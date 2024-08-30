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


    def clean_data(self):
        # Drop unnecessary columns
        self.data.drop(columns=['Unnamed: 0'], inplace=True)
        # Handle missing values if needed
        self.data.dropna(inplace=True)
        # Convert date column to datetime
        self.data['date'] = pd.to_datetime(self.data['date'], format='ISO8601')
        

    def get_article_length(self):
        self.data['headline_length'] = self.data['headline'].apply(len)
        return self.data['headline_length'].describe()

    def count_articles_per_publisher(self):
        return self.data['publisher'].value_counts()
    

    def analyze_publication_dates(self):
        self.data['publication_date'] = self.data['date'].dt.date
        return self.data['publication_date'].value_counts()
    
    def plot_article_statistics(self):
        # Get data from the EDA functions
        self.get_article_length()
        articles_per_publisher = self.count_articles_per_publisher()
        
        # Plotting the statistics
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        sns.histplot(self.data['headline_length'], bins=20, kde=True)
        plt.title('Distribution of Headline Lengths')
        plt.xlabel('Headline Length')
        plt.ylabel('Frequency')

        plt.subplot(1, 2, 2)
        articles_per_publisher.plot(kind='bar')
        plt.title('Number of Articles per Publisher')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')

        plt.tight_layout()
        plt.show()
        


    def sentiment_analysis(self):
        nltk.download('vader_lexicon')
        sia = SentimentIntensityAnalyzer()
        self.data['sentiment'] = self.data['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])
        return self.data['sentiment'].describe()
    

    def plot_sentiment_distribution(self):
        sns.histplot(self.data['sentiment'], kde=True)
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Frequency')
        plt.show()

    def time_series_analysis(self):
        self.data['publication_hour'] = self.data['date'].dt.hour
        return self.data['publication_hour'].value_counts()
    
    def plot_publication_frequency(self):
        publication_frequency = self.data['date'].value_counts().sort_index()
        plt.figure(figsize=(14, 6))
        plt.plot(publication_frequency)
        plt.title('Publication Frequency Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.show()


    def analyze_publishers(self):
        publisher_analysis = self.data.groupby('publisher').size().reset_index(name='article_count')
        return publisher_analysis.sort_values(by='article_count', ascending=False)


