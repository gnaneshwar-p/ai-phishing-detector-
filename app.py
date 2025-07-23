import streamlit as st
from src.model import train_model
from src.preprocess import load_and_preprocess_data
from src.detector import detect_email

st.title("AI Phishing Email Detector")

if "model" not in st.session_state:
    X_train, X_test, y_train, y_test = load_and_preprocess_data("data/phishing_emails.csv")
    st.session_state.model = train_model(X_train, X_test, y_train, y_test)

email_input = st.text_area("Paste email content here:")
if st.button("Detect"):
    result = detect_email(st.session_state.model, email_input)
    st.success(f"Result: {result}")
