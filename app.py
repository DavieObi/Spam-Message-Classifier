import streamlit as st
import joblib
import numpy as np

# Load model and vectorizer
model = joblib.load('spam_classifier_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

# App title
st.set_page_config(page_title="Spam Message Classifier", page_icon="💬", layout="centered")

# Custom background and fonts
page_bg = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f2f2f2, #dfe9f3);
    background-attachment: fixed;
}

.main-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    color: #333;
    margin-bottom: 0.5rem;
}

.sub-title {
    text-align: center;
    font-size: 1rem;
    color: #666;
    margin-bottom: 2rem;
}

.stTextArea label {
    font-weight: 500;
    color: #333;
}

.result-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    text-align: center;
    margin-top: 20px;
}

.spam {
    color: #ff4d4d;
    font-weight: 700;
    font-size: 1.5rem;
}

.ham {
    color: #2ecc71;
    font-weight: 700;
    font-size: 1.5rem;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">📩 Spam Message Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Detect whether a message is Spam or Ham in seconds!</div>', unsafe_allow_html=True)

# Text input
user_input = st.text_area("Enter a message:", height=150, placeholder="Type or paste a message here...")

# Predict button
if st.button("Classify Message"):
    if user_input.strip() == "":
        st.warning("Please enter a message before classifying.")
    else:
        # Vectorize the text
        transformed_input = vectorizer.transform([user_input])

        # Predict
        prediction = model.predict(transformed_input)
        label = 'Spam' if prediction[0] == 1 else 'Ham'

        # Show result
        if label == 'Spam':
            st.markdown(f'<div class="result-box"><p class="spam">🚫 This message is classified as SPAM!</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="result-box"><p class="ham">✅ This message is classified as HAM (Not Spam)</p></div>', unsafe_allow_html=True)
