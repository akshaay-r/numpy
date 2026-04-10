# 🎬 Movie Popularity Prediction (ML Project)

## 📖 Overview

This project builds a Machine Learning model to predict whether a movie is "popular" or not based on its features. It demonstrates a complete ML workflow including data preprocessing, feature engineering, model training, and evaluation.

---

## 📂 Dataset

- Source: Netflix Movies and TV Shows Dataset (Kaggle)
- Contains information such as:
  - Type (Movie / TV Show)
  - Country
  - Release Year
  - Genre and other metadata

---

## 🎯 Objective

- Build a classification model to predict movie popularity
- Understand the end-to-end ML pipeline
- Learn feature selection and model evaluation

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas
- NumPy
- Scikit-learn

---

## 🧹 Data Preprocessing

- Selected relevant features (`type`, `country`, etc.)
- Handled missing values using `dropna()`
- Converted categorical data into numerical format using `get_dummies()`
- Created a target variable `popular`

---

## ⚠️ Important Learning: Data Leakage

Initially, the model achieved 100% accuracy due to **data leakage**, as the `release_year` feature was directly used to create the target variable.

This issue was fixed by removing the `release_year` column from the feature set.

---

## 🤖 Model Used

- Logistic Regression

---

## 📊 Model Evaluation

- Accuracy Score achieved: ~67% (after fixing data leakage)
- Demonstrates a working baseline ML model

---

## 🔍 Key Learnings

- Understanding of ML pipeline (data → model → prediction)
- Importance of proper feature selection
- Handling categorical data
- Identifying and fixing data leakage

---

## 🚀 Future Improvements

- Use better target definition (real popularity metrics)
- Try advanced models like Random Forest or XGBoost
- Feature engineering for improved accuracy
- Build a web interface for predictions

---

## 📁 Project Structure

Movie-Popularity-ML/
│
├── Data/
│ └── netflix_titles.csv
│
├── notebook/
│ └── analysis.ipynb
│
└── README.md

---

## 🙌 Author

Aki
