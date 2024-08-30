# Financial News Sentiment Analysis and Stock Market Correlation

## Overview

This project will analyze a significant amount of financial news data to find correlations between news sentiment and stock market movements. The analysis attempts to improve predictive analytics capabilities by improving financial forecasting accuracy and operational efficiency using advanced data analysis methodologies. This project's tasks include components of Data Engineering, Financial Analytics, Machine Learning Engineering, and more.

### Key Objectives
- **Sentiment Analysis:** Conduct sentiment analysis on financial news items to determine the sentiment (positive, negative, neutral) and correlate it with stock price fluctuations.
- **Correlation Analysis:** Create statistical correlations between sentiment produced from news stories and the relevant stock price fluctuations.
- **Predictive Analytics:** Use sentiment analysis to recommend investing strategies based on the relationship between news sentiment and stock market patterns.

## Folder Structure

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
├── notebooks/
│   ├── __init__.py
│   ├── EDA.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    ├── data_analysis.py
    └── README.md
```

## Project Setup

### Prerequisites

Ensure you have Python 3.8 or later installed. Additionally, you'll need to install the required Python packages listed in the `requirements.txt` file.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shewanek/week_1.git
   cd week_1
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv week_1
   week_1\Scripts\activate       # On macOS/Linux: source week_1/bin/activate  
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


### Running the Project

1. **Perform Exploratory Data Analysis (EDA)**:
   - Navigate to the `notebooks/` directory and run the Jupyter notebooks to explore the dataset.

2. **Run the Sentiment Analysis**:
   - Use the scripts in the `src/` directory to perform sentiment analysis on the financial news headlines.

3. **Execute Unit Tests**:
   - Run unit tests using GitHub Actions to ensure code quality.

4. **Run the Full Pipeline**:
   - Use the `main.py` script to execute the complete analysis pipeline.


### CI/CD Setup

This project uses GitHub Actions for Continuous Integration (CI). The workflow is defined in `.github/workflows/unittests.yml` and includes:
- Running unit tests.
- Linting and code quality checks.
- Automated deployment (if applicable).

## Tasks and Milestones

### Task 1: Git and GitHub

- **Objective**: Set up a Python environment, Git version control, and CI/CD pipeline.
- **Deliverables**:
  - A GitHub repository with a clear folder structure.
  - At least one new branch `task-1`.
  - Committed and pushed work with descriptive commit messages.
- **Key KPIs**:
  - Dev environment setup and relevant skills demonstrated.



### Task 2: Quantitative Analysis using PyNance and TA-Lib

- **Objective**: Apply technical indicators using TA-Lib and analyze financial data.
- **Deliverables**:
  - A new branch `task-2` with all necessary code and documentation.
  - Detailed visualizations of the financial data.
- **Key KPIs**:
  - Accuracy and completeness of data analysis.

### Task 3: Correlation between News and Stock Movement

- **Objective**: Align financial news and stock data by dates and conduct correlation analysis.
- **Deliverables**:
  - A new branch `task-3` with sentiment analysis and correlation analysis.
  - Final report with actionable insights based on correlation analysis.
- **Key KPIs**:
  - Accuracy in sentiment analysis and strength of correlations discovered.

## Reports and Documentation

- **Interim Report**: Covers progress up to Task 2. It includes the initial findings from the exploratory data analysis and the first round of sentiment analysis.
- **Final Report**: A comprehensive report that includes all tasks, final insights, and recommendations for using sentiment analysis as a predictive tool for stock market trends.


