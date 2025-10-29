---

# 📩 Spam Message Classifier

## 📘 Project Overview

The **Spam Message Classifier** is a machine learning-based web application designed to detect whether an incoming message is **Spam** or **Ham (Not Spam)**. Built using **Python**, **Scikit-learn**, and **Streamlit**, the project leverages natural language processing (NLP) techniques to analyze textual content and predict its category in real time.

The model was trained on a labeled dataset containing both spam and non-spam messages, achieving an impressive **96.68% accuracy** on the test data.

---

## 🚨 Problem Statement

With the rapid growth of digital communication, email and SMS spam messages have become a major issue for users and service providers alike. These unwanted messages can clutter inboxes, waste time, and sometimes contain malicious links or phishing attempts.

Manual filtering of spam is inefficient and impractical at scale, highlighting the need for an **automated and intelligent solution** that can accurately classify messages as spam or legitimate.

---

## 🎯 Project Objective

The primary goal of this project is to develop a **machine learning model** capable of identifying spam messages with high precision and recall.
To achieve this, the project aims to:

* **Preprocess text data** by cleaning, lowercasing, and removing punctuation.
* **Extract meaningful features** from messages using the **TF-IDF Vectorizer**.
* **Train a Naive Bayes classifier** to distinguish between spam and non-spam messages.
* **Evaluate the model** using metrics such as accuracy, precision, recall, and F1-score.
* **Deploy the model** using **Streamlit** for an intuitive web-based user experience.

---

## 🧠 Model Performance

* **Algorithm Used:** Multinomial Naive Bayes
* **Feature Extraction:** TF-IDF (Term Frequency–Inverse Document Frequency)
* **Accuracy:** 96.68%
* **Classification Report:**

| Category | Precision | Recall | F1-Score |
| -------- | --------- | ------ | -------- |
| Ham      | 0.96      | 1.00   | 0.98     |
| Spam     | 1.00      | 0.75   | 0.86     |

---

## 🚀 Deployment

The model and vectorizer were saved using **Joblib** and integrated into a **Streamlit app**.
The app features:

* A clean and minimal **Poppins** font interface.
* A gradient background for visual appeal.
* Real-time message classification with clear feedback indicators.

Users can simply input a message, click **“Classify Message”**, and instantly see whether it’s **Spam 🚫** or **Ham ✅**.

---

## ✅ Conclusion

This project demonstrates how **machine learning and NLP** can effectively combat spam communication by automating message classification.
With its strong accuracy and seamless deployment, the **Spam Message Classifier** serves as a practical and scalable solution to digital message filtering. Future improvements could include expanding to multilingual datasets or integrating deep learning models for enhanced context understanding.

---

