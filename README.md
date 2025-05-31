# PricePeek-Laptop Price Predictor

A machine learning web application that predicts the price of a laptop based on its specifications. This project evaluates multiple regression algorithms to find the best-performing model and deploys the final solution with an interactive Streamlit interface.

## 🚀 Live Demo
https://pricepeek-k6pu.onrender.com/

---

## 📈 Overview

The Laptop Price Predictor project uses a dataset of laptop specifications and prices to train and compare various regression models. After evaluating performance, **Random Forest Regressor** was selected as the best fit for the prediction task. The model is exported using `joblib` and integrated with a user-friendly **Streamlit UI**.

---

## 🧠 Machine Learning Models Tested

- 📉 Linear Regression  
- 🧮 Ridge Regression  
- 🧲 Lasso Regression  
- 👥 K-Nearest Neighbors Regressor  
- 🌳 Random Forest Regressor ✅ *(Best Performing)*  
- ⚡ XGBoost Regressor  

---

## 🧪 Model Evaluation

All models were tested using performance metrics such as:
- **R² Score**
- **Mean Absolute Error (MAE)**
- **Cross-validation**

After evaluation, **Random Forest Regressor** achieved the best balance of accuracy and generalization.

---

## 🛠️ Tech Stack

- **Python** – Core scripting
- **Pandas, NumPy** – Data preprocessing
- **Scikit-learn** – Model training and evaluation
- **XGBoost** – Gradient boosting model
- **Joblib** – Model serialization
- **Streamlit** – Web UI for user interaction

---

## 🎯 Features

- Predicts laptop price based on:
  - **Company** – Manufacturer brand (e.g., HP, Asus)
  - **TypeName** – Device type (e.g., Notebook, Ultrabook)
  - **Ram** – RAM in GB
  - **Weight** – Laptop weight in kg
  - **Touchscreen** – 0 or 1 (No/Yes)
  - **Ips** – IPS panel indicator (0 or 1)
  - **ppi** – Pixels per inch (screen sharpness)
  - **Cpu brand** – e.g., Intel Core i5, AMD Processor
  - **HDD** – Hard disk drive storage (in GB)
  - **SSD** – Solid state drive storage (in GB)
  - **Gpu Brand** – GPU manufacturer (Intel, AMD, etc.)
  - **os** – Operating System (Windows, Linux, etc.)

- Simple, responsive web interface using Streamlit  
- Live prediction with instant results  

---
## 🖥️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/TaniyaGoyat/Laptop_Price_Predictor.git
   cd Laptop_Price_Predictor

