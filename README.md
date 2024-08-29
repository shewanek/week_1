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



