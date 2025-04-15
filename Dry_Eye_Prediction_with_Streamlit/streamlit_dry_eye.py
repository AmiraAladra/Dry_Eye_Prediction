import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model
with open("models/rf_de.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load dataset for visualization
df = pd.read_csv("data/raw/Dry_Eye_Dataset_Phase1.csv")

# Define feature columns for prediction
dry_eye_features = [
    'Smart device before bed', 'Discomfort Eye-strain', 'Redness in eye',
    'Itchiness/Irritation in eye', 'Gender_F', 'Gender_M', 'Stress level_1',
    'Stress level_2', 'Stress level_3', 'Stress level_4', 'Stress level_5']

# Streamlit App UI
st.title("🌟 Dry Eye Disease Prediction App ")
st.write("Enter details to check if you are at risk for Dry Eye Disease.")

# Sidebar for user input
st.sidebar.header("User Input Features")
smart_device = st.sidebar.selectbox("Smart device before bed", ["Yes", "No"])
eye_strain = st.sidebar.selectbox("Discomfort Eye-strain", ["Yes", "No"])
redness = st.sidebar.selectbox("Redness in eye", ["Yes", "No"])
itchiness = st.sidebar.selectbox("Itchiness/Irritation in eye", ["Yes", "No"])
gender = st.sidebar.radio("Gender", ["Male", "Female"])
stress = st.sidebar.slider("Stress Level (1-5)", 1, 5, 3, key="stress_slider")

# Convert categorical inputs into numeric
smart_device = 1 if smart_device == "Yes" else 0
eye_strain = 1 if eye_strain == "Yes" else 0
redness = 1 if redness == "Yes" else 0
itchiness = 1 if itchiness == "Yes" else 0
gender_f = 1 if gender == "Female" else 0
gender_m = 1 if gender == "Male" else 0

# Stress Level (1 to 5) – One-hot encoding for stress level
stress_levels = [0, 0, 0, 0, 0]  # Default [0, 0, 0, 0, 0]
stress_levels[stress - 1] = 1  # One-hot encode the selected stress level

# Prepare the input data as a DataFrame
input_data = pd.DataFrame([[smart_device, eye_strain, redness, itchiness, gender_f, gender_m] + stress_levels],
                          columns=dry_eye_features)

# Predict the Dry Eye Disease risk
if st.sidebar.button("Predict Dry Eye Disease"):
    prediction = model.predict(input_data)[0]
    result = "🔴 High Risk of Dry Eye Disease" if prediction == 1 else "🟢 Low Risk of Dry Eye Disease"
    st.subheader("Prediction Result")
    st.markdown(f"## {result}")

# 📊 **Stress Level Distribution**
st.subheader("📊 Stress Level Distribution")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.countplot(x='Stress level', data=df, ax=ax1, palette="coolwarm")
ax1.set_title("Distribution of Stress Levels")
st.pyplot(fig1)

# 📊 **Gender vs. Dry Eye Disease**
st.subheader("📊 Gender vs. Dry Eye Disease")
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.countplot(x='Gender', hue='Dry Eye Disease', data=df, ax=ax2, palette="coolwarm")
ax2.set_title("Gender vs. Dry Eye Disease")
st.pyplot(fig2)

# 📊 **Dry Eye Disease vs. Discomfort Eye-strain**
st.subheader("📊 Dry Eye Disease vs. Discomfort Eye-strain")
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.countplot(x='Dry Eye Disease', hue='Discomfort Eye-strain', data=df, ax=ax3, palette="Blues")
ax3.set_title("Dry Eye Disease vs. Discomfort Eye-strain")
st.pyplot(fig3)

# 📊 **Dry Eye Disease vs. Redness in Eye**
st.subheader("📊 Dry Eye Disease vs. Redness in Eye")
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.countplot(x='Dry Eye Disease', hue='Redness in eye', data=df, ax=ax4, palette="Greens")
ax4.set_title("Dry Eye Disease vs. Redness in Eye")
st.pyplot(fig4)

# 📊 **Dry Eye Disease vs. Itchiness/Irritation in Eye**
st.subheader("📊 Dry Eye Disease vs. Itchiness/Irritation in Eye")
fig5, ax5 = plt.subplots(figsize=(8, 5))
sns.countplot(x='Dry Eye Disease', hue='Itchiness/Irritation in eye', data=df, ax=ax5, palette="Oranges")
ax5.set_title("Dry Eye Disease vs. Itchiness/Irritation in Eye")
st.pyplot(fig5)
