## Try it
https://dry-eye-predictor-amira.streamlit.app/

# 👁️ Dry Eye Disease Prediction using Machine Learning

This project leverages **machine learning** to predict the likelihood of developing **Dry Eye Disease (DED)** based on individual lifestyle factors, physiological indicators, and screen exposure habits. A **Streamlit web app** is included for interactive predictions.

---

## 📌 Project Overview

With increased digital screen usage and stressful lifestyles, more people are experiencing health issues like **Dry Eye Disease (DED)** and poor sleep. This project uses real-world data to build a **predictive model for DED**, helping users understand their risk and adopt preventive habits.

While an initial secondary goal was to predict **sleep quality**, that part was dropped due to low model performance (< 20% accuracy). The final project focuses on DED.

---

## 🎯 Objective

- 🧠 **Predict Dry Eye Disease** using machine learning based on:
  - Screen time and device usage
  - Sleep and eye strain symptoms
  - Lifestyle and physiological factors

- 🌐 Deploy an **interactive Streamlit app** to enable user input and prediction
- 📈 Create a **Power BI dashboard** for visual analytics and insights

---

## 🧾 Dataset Overview

- 📥 **Source**: [Kaggle - Dry Eye Disease Dataset](https://www.kaggle.com/datasets/dakshnagra/dry-eye-disease)
- 🔢 **Records**: 20,001 rows × 26 columns
- ✅ **Clean**: No missing values or duplicates

---

## 🧪 Data Processing

### 🔹 Feature Engineering
- **Blood Pressure Splitting** → Systolic & Diastolic BP
- **BMI Calculation** → Derived from weight and height
- **Categorical Encoding** → Gender, stress level (one-hot), and Y/N fields (binary)

### 🔹 Feature Selection Techniques
- Correlation Heatmap
- Recursive Feature Elimination (RFE)
- Random Forest Feature Importance
- Chi-Square Test (for categorical vars)

### 🔹 Final Selected Features
**For Dry Eye Prediction**:
- Discomfort Eye-strain  
- Redness in Eye  
- Itchiness/Irritation  
- Average Screen Time  
- Physical Activity  
- Sleep Duration  
- Systolic BP  

---

## 🤖 Model Building

### Models Evaluated:
- Logistic Regression → Accuracy: 68%  
- Neural Network → Accuracy: 70%  
- ✅ **Random Forest Classifier** → **Best model, accuracy: 70%**

The Random Forest model was chosen for its balance of performance and efficiency.

---

## 💻 Code Architecture

Structured using modularized Python files in **VS Code**:

- `data_processing.py` – Load and preprocess the dataset
- `feature_engineering.py` – Feature transformation and selection
- `model_training.py` – Train and evaluate the Random Forest model
- `predict.py` – Load model and perform live predictions
- `app.py` – Streamlit interface for the user
- Error handling is included throughout for robustness

---

## 🌐 Streamlit Web App

An easy-to-use **web interface** built using Streamlit:
- Users enter personal and lifestyle information
- The app predicts their **Dry Eye Disease risk**
- Includes interactive charts and visual insights

To run:
```bash
streamlit run app.py

## 🔍 Key Insights & Findings
🔵 Smart device use before bed significantly increases DED risk

🔴 Females are slightly more prone to DED symptoms

⚠️ Stress strongly correlates with eye discomfort

📉 Poor sleep and screen overuse contribute to DED symptoms

## 💡 Recommendations
Limit screen time before bed

Practice stress management (meditation, exercise)

Promote awareness of early symptoms

Gather more data to improve model accuracy

## 🧠 What I Learned
Real-world feature engineering and model evaluation

Using statistical & ML techniques for feature selection

Building an interactive Streamlit app

Visual storytelling with Power BI
