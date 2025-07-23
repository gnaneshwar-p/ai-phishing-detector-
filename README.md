# ai-phishing-detector-
This project uses machine learning to detect phishing emails based on their content. Built using Python, scikit-learn, and Streamlit.

## Features
- Preprocesses real-world email data
- Trains ML model to detect phishing
- Provides a dashboard interface
- Simulates logging like a SOC

## Setup
```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Example Dataset
Place a CSV file at `data/phishing_emails.csv` with the following structure:
```
text,label
"Your account has been suspended...",phishing
"Monthly newsletter from your bank",legitimate
```
