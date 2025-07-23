import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    return text

def load_and_preprocess_data(csv_path):
    df = pd.read_csv(csv_path)
    df['clean_text'] = df['text'].apply(clean_text)
    X = df['clean_text']
    y = df['label']
    return train_test_split(X, y, test_size=0.2, random_state=42)
