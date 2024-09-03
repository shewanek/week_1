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
