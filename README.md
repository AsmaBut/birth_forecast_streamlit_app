
# 📊 Birth Forecast Streamlit App  

This project is an **interactive forecasting dashboard** built with **Streamlit** to predict birth rates based on historical trends, economic indicators, and healthcare metrics.  
It allows policymakers and analysts to explore model predictions, key drivers, and data insights.

---

## 🚀 Features
- **Forecasting Model**: XGBoost model trained on different features  
- **Interactive Dashboard**: View predictions, change inputs, and visualize results in real-time  
- **Explainability**: Feature importance insights from SHAP analysis  
- **Automated Pipeline**: Easily updatable with new monthly data  

---

## 📂 Repository Structure
`

birth\_forecast\_streamlit\_app/
│── birth\_forecast\_dashboard/
│   ├── best\_model.pkl             # Trained XGBoost model
│   ├── dashboard.py                # Streamlit app code
│   ├── model\_features.pkl          # Feature names for model
│   ├── test\_model.py               # Script to test model locally
│── Model Interpretation.ipynb      # SHAP & model explainability analysis
│── Model\_Building\_and\_Evaluation\_and\_Comparison.ipynb  # Model training & evaluation
│── dataset-merge.py                # Dataset preprocessing script
│── final\_merged\_dataset.csv        # Cleaned & merged dataset

`


## ⚙️ Installation & Running Locally

### 1️⃣ Clone the repository
``bash
git clone https://github.com/AsmaBut/birth_forecast_streamlit_app.git
cd birth_forecast_streamlit_app
```


### 3️⃣ Run the app locally

```bash
python -m streamlit run birth_forecast_dashboard/dashboard.py
```

---

## 🌐 Deployment

This app is deployed to **Streamlit Community Cloud**:
(https://asmabut-birth-forecast-birth-forecast-dashboarddashboard-5zxc1q.streamlit.app/)
---

## 📊 Model Performance

* **Random Forest R²**: 0.9623
* **XGBoost R²**: 0.9699
* **Top features**:

  1. `Births_rolling_mean_3`
  2. `Births_lag6_rolling_mean_3`
  3. `Births_lag1`

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **XGBoost**
* **Pandas, NumPy**
* **SHAP (Explainability)**

---

## 📌 Author

**Asma Butt**


