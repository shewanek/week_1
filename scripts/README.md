# Financial News Data Analysis Script

## Overview
The `data_analysis.py` script provides a structured approach to analyzing a financial news dataset. This script is designed to be modular, allowing easy use of various functions for performing Exploratory Data Analysis (EDA) and sentiment analysis on financial news headlines.

## Features
- **Data Cleaning**: Automatically handles missing values, unnecessary columns, and converts date columns to the appropriate format.
- **Basic Statistics**: Provides descriptive statistics for the dataset.
- **Article Length Analysis**: Computes the length of headlines and provides statistics on headline lengths.
- **Publisher Analysis**: Counts the number of articles per publisher and analyzes publication trends.
- **Sentiment Analysis**: Uses the NLTK library to perform sentiment analysis on headlines, scoring them as positive, negative, or neutral.
- **Time Series Analysis**: Analyzes the time distribution of news articles to find patterns in publication times.
- **Visualization**: Includes methods for visualizing sentiment distribution.

## Dependencies
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `nltk`

Make sure to install the required packages before running the script:
```bash
pip install pandas numpy matplotlib seaborn nltk

## Task 2

# Stock Data Analysis and Sentiment Correlation - Python Script

## Overview
This Python script is designed to perform a comprehensive analysis of stock data and financial news sentiment. It contains classes and methods to load data, calculate technical indicators, visualize trends, and analyze the correlation between news sentiment and stock price movements.

## Script Structure

### 1. `FinancialNewsEDA` Class
This class handles financial news data, including loading, analyzing, and performing sentiment analysis on the headlines.

#### Methods:
- **`__init__(self, file_path)`**: Initializes the class with the file path containing the financial news data.
  
- **`load_data(self)`**: Loads the news data from the CSV file into a DataFrame.
  
- **`data_descriptive(self)`**: Provides descriptive statistics of the news dataset, checking for missing values, duplicates, and data types.
  
- **`clean_data(self)`**: Cleans the news dataset by dropping unnecessary columns, handling missing values, and converting date columns to datetime format.
  
- **`get_article_length(self)`**: Calculates and returns descriptive statistics of the headline lengths in the dataset.
  
- **`count_articles_per_publisher(self)`**: Returns the count of articles published by each publisher.
  
- **`analyze_publication_dates(self)`**: Analyzes the publication dates of the articles.
  
- **`plot_article_statistics(self)`**: Visualizes the number of articles published over time and by day of the week.
  
- **`sentiment_analysis(self)`**: Performs sentiment analysis on the headlines using NLTK's VADER sentiment analyzer and returns descriptive statistics of the sentiment scores.
  
- **`plot_sentiment_distribution(self)`**: Visualizes the distribution of sentiment categories (Negative, Neutral, Positive).
  
- **`word_frequency(self)`**: Analyzes and visualizes the most frequent words in the headlines.
  
- **`time_series_analysis(self)`**: Analyzes the publication times of articles.
  
- **`plot_publication_frequency(self)`**: Visualizes the frequency of publications over time.
  
- **`analyze_publishers(self)`**: Analyzes and returns the number of articles published by each publisher and their domains.
  
- **`plot_publisher_analysis(self)`**: Visualizes the top publishers by article count.
  
- **`save_to_csv(self, output_path)`**: Saves the processed data to a CSV file. The default path is set to `data/processed_financial_news.csv`.

## Usage
1. **Stock Data Analysis**:
   - Initialize the `StockEDA` class with the folder path containing your stock data CSV files.
   - Use the `load_data` method to load the data.
   - Apply the `apply_ta_indicators` and `calculate_financial_metrics` methods to analyze the data.
   - Use `visualize_stocks` and `plot_financial_metrics` to visualize the results.

2. **Financial News Analysis**:
   - Initialize the `FinancialNewsEDA` class with the file path to your news data.
   - Use `load_data` and `clean_data` to prepare the data.
   - Perform sentiment analysis using `sentiment_analysis`.
   - Visualize the data using `plot_article_statistics`, `plot_sentiment_distribution`, and `plot_publisher_analysis`.
   - Save the processed data using `save_to_csv`.

### 2. `StockEDA` Class
This class is focused on analyzing stock data, calculating technical indicators, and visualizing trends.

#### Methods:
- **`__init__(self, folder_path)`**: Initializes the class with the folder path containing the stock data CSV files.
  
- **`load_data(self)`**: Loads all CSV files from the specified folder, extracts the stock symbols from the filenames, and concatenates the data into a single DataFrame.
  
- **`data_descriptive(self)`**: Provides descriptive statistics of the dataset, including checking for missing values, duplicates, and data types.
  
- **`calculate_technical_indicators(self, df)`**: Calculates essential technical indicators such as Simple Moving Average (SMA), Exponential Moving Average (EMA), Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD).
  
- **`apply_ta_indicators(self)`**: Applies the technical indicators to each stock symbol in the dataset.
  
- **`visualize_stocks(self, df)`**: Visualizes the stock price along with SMA and EMA for each stock symbol.
  
- **`calculate_financial_metrics(self)`**: Calculates financial metrics such as daily returns, rolling volatility, moving average, and cumulative returns.
  
- **`plot_financial_metrics(self)`**: Visualizes the calculated financial metrics for each stock symbol.


# 3 Correlation Analysis Between Financial News Sentiment and Stock Movements

## Overview
This Python script is designed to analyze the correlation between financial news sentiment and stock price movements. It loads financial news data and stock data, prepares the data for analysis, calculates the Pearson correlation coefficient for each stock, and visualizes the results. The script is particularly useful for understanding how news sentiment might impact stock performance.

## Script Structure

### 1. `Corr_analysis` Class
The `Corr_analysis` class performs the primary analysis by loading the data, preparing it, calculating correlations, and visualizing the results.

#### Methods:
- **`__init__(self, financial_data_path, stock_data_path)`**: Initializes the class with file paths to the financial news data and stock data.

- **`load_data(self)`**: Loads the financial news data and stock data from the specified CSV files and returns the loaded DataFrames.

- **`prepare_data(self)`**: Prepares the data for analysis by converting date columns to datetime format, aligning dates, calculating average daily sentiment, and calculating daily stock returns. It then merges the sentiment data with the stock data on date and stock symbol.

- **`calculate_correlation(self)`**: Calculates the Pearson correlation coefficient between daily sentiment scores and daily stock returns for each stock symbol. It returns the correlation results.

- **`plot_correlation(self, correlation_results)`**: Plots the correlation results using a bar plot. The plot shows the Pearson correlation coefficient for each stock symbol, indicating the strength and direction of the relationship between sentiment scores and stock returns.

- **`scatter_plot(self)`**: Creates a scatter plot of sentiment scores versus daily stock returns for all stock symbols. This plot visualizes the relationship between sentiment and stock returns across different stocks.

- **`scatter_plot_each(self)`**: Generates individual scatter plots for each stock symbol, visualizing the relationship between sentiment scores and daily stock returns for each stock.


