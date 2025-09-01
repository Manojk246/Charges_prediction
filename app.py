import streamlit as st
import pickle
import numpy as np

# ----------------------------
# 1. Load Trained Model
# ----------------------------
with open("trained_model.sav", "rb") as f:
    model = pickle.load(f)

# ----------------------------
# 2. App Title
# ----------------------------
st.title("💰 Medical Insurance Charges Predictor")
st.write("This app predicts **medical charges** based on personal and lifestyle factors.")

# ----------------------------
# 3. Input Features
# ----------------------------
age = st.number_input("Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sex", options=["Male", "Female"])
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", options=["Yes", "No"])
region = st.selectbox("Region", options=["northeast", "northwest", "southeast", "southwest"])

# ----------------------------
# 4. Encode Inputs (match training)
# ----------------------------
sex_encoded = 1 if sex == "Male" else 0
smoker_encoded = 1 if smoker == "Yes" else 0

# Encode region as numbers 0–3 (since training used a single 'region' column)
region_mapping = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region_encoded = region_mapping[region]

# Final feature order (must match training)
features = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])

# ----------------------------
# 5. Prediction
# ----------------------------
if st.button("🔮 Predict Charges"):
    prediction = model.predict(features)
    st.success(f"✅ Estimated Medical Charges: **${prediction[0]:,.2f}**")
