```markdown
# Exploratory Data Analysis Notebook
```
## Overview
The `EDA.ipynb` notebook is designed to perform an in-depth exploratory data analysis (EDA) on a financial news dataset. The notebook leverages the `FinancialNewsAnalysis` class from the `data_analysis.py` script to conduct various analyses, including basic statistics, sentiment analysis, and time series analysis.

## Features
- **Interactive Analysis**: Allows you to interactively explore and visualize the data.
- **Descriptive Statistics**: Analyze the distribution of headline lengths, publication times, and article counts per publisher.
- **Sentiment Analysis**: Evaluate the sentiment of headlines and visualize sentiment distributions.
- **Publisher Analysis**: Identify trends and patterns among publishers, such as the frequency of articles.

## Dependencies
- `os`
- `sys`


## task 2
# Stock Data Preparation and Technical Analysis

## Overview
This project focuses on preparing and analyzing stock data to calculate essential financial metrics and technical indicators. The goal is to provide insights that can assist in making data-driven decisions in trading strategies.

## Dataset
The stock dataset used in this analysis contains the following columns:
- **Date**: The date of the stock trading day.
- **Open**: Opening price of the stock.
- **High**: The highest price of the stock during the day.
- **Low**: The lowest price of the stock during the day.
- **Close**: The closing price of the stock.
- **Adj Close**: The adjusted closing price, accounting for any corporate actions like dividends or stock splits.
- **Volume**: The number of shares traded during the day.
- **Dividends**: Any dividends paid out.
- **Stock Splits**: Any stock splits that occurred.

### Stock Symbol Extraction
The stock symbol is extracted from the file name of the data. Each file represents a specific stock's trading data.

## Calculated Technical Indicators
Several key financial metrics were calculated to provide insights into the stock's performance:

1. **Daily Returns**: 
   - The percentage change in the closing prices from one day to the next. This metric is crucial for understanding short-term price movements.

2. **Rolling Volatility**: 
   - The standard deviation of the daily returns, calculated over a 20-day window. This indicator helps in understanding the stock's risk by showing how much the price fluctuates.

3. **Moving Average**: 
   - The 20-day moving average of the closing prices. This is a commonly used indicator to smooth out price data and identify trends over time.

4. **Cumulative Returns**: 
   - Calculated as the cumulative product of daily returns. This metric provides insight into the overall growth or decline of the stock's value over time.

## Visualization
Several visualizations were created to represent the calculated indicators. These charts help identify trends and patterns in the stock data:

- **Closing Price with Moving Average**: This plot shows the stock's closing price along with its 20-day moving average, helping to identify trends.

- **Daily Returns**: This plot shows the daily percentage changes in stock prices, giving insights into short-term volatility.

- **Rolling Volatility**: A plot of the rolling standard deviation of daily returns, providing an understanding of the stock's risk.

- **Cumulative Returns**: A plot of cumulative returns over time, showing the overall growth or decline in stock value.

These visualizations are vital tools for traders and analysts to make informed decisions based on historical stock data.

## Task 3
# Correlation Analysis Between News Sentiment and Stock Movements

## Overview
Task 3 focuses on analyzing the relationship between news sentiment and stock price movements. By aligning sentiment data from financial news articles with corresponding stock data, the goal was to calculate and visualize statistical correlations between these two variables.

## Data Alignment
The sentiment scores derived from financial news articles (Task 1) were aligned with stock price data (Task 2). This alignment was based on:
- **Publication Dates**: Ensuring that the sentiment score corresponds to the stock's performance on the same date.
- **Stock Symbols**: Matching sentiment data to the correct stock.

This careful alignment ensures the accuracy of the correlation analysis between news sentiment and stock movements.

## Correlation Calculation
The Pearson correlation coefficient was used to measure the strength and direction of the relationship between news sentiment and stock price movements. The results for each stock symbol are as follows:

- **AAPL (Apple)**: 0.089
- **AMZN (Amazon)**: 0.163
- **GOOG (Google)**: 0.187
- **NVDA (Nvidia)**: 0.213
- **TSLA (Tesla)**: 0.163

### Interpretation:
- **Positive Correlations**: All stocks showed a positive correlation, suggesting that as news sentiment becomes more positive, stock returns also tend to increase.
- **Stronger Relationships**: Stocks like **NVDA** showed a relatively stronger relationship between sentiment and stock returns, while **AAPL** had a weaker correlation.

## Visualization of Correlations
To visualize these relationships, scatter plots were created for each stock symbol. These plots display the sentiment scores on the x-axis and daily stock returns on the y-axis, providing a visual representation of the correlation:

- **Scatter Plots**: Show the relationship between sentiment scores and daily stock returns for each stock symbol. The scatter plots help in visually interpreting the correlation, indicating how much influence sentiment might have on stock movements.



