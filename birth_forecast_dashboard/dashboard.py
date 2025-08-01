import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -------------------------------
# 1️⃣ Load Model & Feature List
# -------------------------------
st.title("📊 Birth Forecast Dashboard")

try:
    import os

BASE_DIR = os.path.dirname(__file__)  # folder where dashboard.py is located
model_path = os.path.join(BASE_DIR, "best_model.pkl")
features_path = os.path.join(BASE_DIR, "model_features.pkl")

try:
    model = joblib.load(model_path)
    feature_names = joblib.load(features_path)
    st.success("✅ Model & features loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model or features: {e}")
    st.stop()

    st.success("✅ Model & features loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model or features: {e}")
    st.stop()

# -------------------------------
# 2️⃣ User Input for Important Features
# -------------------------------
st.subheader("Enter Key Inputs for Forecast")

# Collect only important inputs (others will be filled as 0)
cpi = st.number_input("CPI Index", value=100.0)
unemployment = st.number_input("Unemployment Rate (%)", value=5.0)
births_last_month = st.number_input("Births Last Month", value=5000)
diabetes = st.number_input("Diabetes %", value=8.0)
induction = st.number_input("Induction %", value=20.0)

# -------------------------------
# 3️⃣ Create Full Feature DataFrame
# -------------------------------
# Start with all zeros
input_data = pd.DataFrame(np.zeros((1, len(feature_names))), columns=feature_names)

# Fill only key features
if "cpi index" in input_data.columns:
    input_data["cpi index"] = cpi
if "UnemploymentRate" in input_data.columns:
    input_data["UnemploymentRate"] = unemployment
if "Births_lag1" in input_data.columns:
    input_data["Births_lag1"] = births_last_month
if "Diabetes %" in input_data.columns:
    input_data["Diabetes %"] = diabetes
if "Induction %" in input_data.columns:
    input_data["Induction %"] = induction

# -------------------------------
# 4️⃣ Prediction
# -------------------------------
if st.button("Predict Births"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"📈 Predicted Births: {prediction:.0f}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
