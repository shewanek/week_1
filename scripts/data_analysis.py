import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
from wordcloud import WordCloud

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
        self.data['day_of_week'] = self.data['date'].dt.day_name()
        articles_per_weekday = self.data['day_of_week'].value_counts()

        # Preparing data for line chart
        articles_per_date = self.data['date'].value_counts().sort_index()

        # Plotting the statistics
        plt.figure(figsize=(14, 6))

        plt.subplot(2, 1, 1)
        sns.lineplot(x=articles_per_date.index, y=articles_per_date.values)
        plt.title('Number of Articles Published Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45, ha='right')

        plt.subplot(2, 1, 2)
        articles_per_weekday.plot(kind='bar', color='skyblue')
        plt.title('Number of Articles by Day of the Week')
        plt.xlabel('Day of Week')
        plt.ylabel('Number of Articles')

        plt.tight_layout()
        plt.show()

        
    def sentiment_analysis(self):
        nltk.download('vader_lexicon')
        sia = SentimentIntensityAnalyzer()
        self.data['sentiment'] = self.data['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])
        return self.data['sentiment'].describe()
    
    def plot_sentiment_distribution(self):
        # Categorize sentiments
        self.data['sentiment_category'] = pd.cut(
            self.data['sentiment'],
            bins=[-1, -0.05, 0.05, 1],
            labels=['Negative', 'Neutral', 'Positive']
        )
        
        # Plot the sentiment distribution
        plt.figure(figsize=(8, 6))
        sns.countplot(x='sentiment_category', data=self.data, palette={"Negative": "red", "Neutral": "gray", "Positive": "green"})
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment Category')
        plt.ylabel('Count')
        plt.show()

    def word_frequency(self):
        word_freq = Counter(" ".join(self.data['headline']).split())
        common_words = pd.DataFrame(word_freq.most_common(20), columns=['Word', 'Frequency'])

        # Plot the word frequency
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Frequency', y='Word', data=common_words, palette='magma')
        plt.title('Top 20 Most Frequent Words in Headlines')
        plt.xlabel('Frequency')
        plt.ylabel('Word')
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
        self.data['domain'] = self.data['publisher'].apply(lambda x: x.split('@')[-1] if '@' in x else x)
        publisher_analysis = self.data.groupby(['publisher', 'domain']).size().reset_index(name='article_count')
        return publisher_analysis.sort_values(by='article_count', ascending=False)
    
    def plot_publisher_analysis(self):
        publisher_analysis = self.analyze_publishers().head(10)
        plt.figure(figsize=(12, 6))
        sns.barplot(data=publisher_analysis, x='publisher', y='article_count', hue='domain', dodge=False, palette='viridis')
        plt.title('Top 10 Publishers by Article Count')
        plt.xlabel('Publisher')
        plt.ylabel('Article Count')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    