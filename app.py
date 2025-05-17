import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the pipeline and data
pipe = joblib.load('pipe.joblib')
df = joblib.load('df.joblib')  # Assuming df.joblib has preprocessed DataFrame or for dropdown options

df = pd.read_csv('new_laptop_data.csv')  # or however you load the data

# Streamlit app title
st.title("Laptop Price Predictor")

# Input selections
company = st.selectbox('Brand', df['Company'].unique())
type = st.selectbox('Laptop Type', df['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input("Weight of the laptop")
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS', ['No', 'Yes'])
screen_size = st.number_input('Screen Size')
resolution = st.selectbox(
    'Screen Resolution',
    ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440']
)
cpu = st.selectbox('CPU', df['Cpu brand'].unique())
hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU', df['Gpu Brand'].unique())
os = st.selectbox('OS', df['os'].unique())

# Predict button
if st.button('Predict Price'):
    # Convert Yes/No to 1/0
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size if screen_size else 0

    # Construct input DataFrame with proper column names
    query = pd.DataFrame([{
        'Company': company,
        'TypeName': type,
        'Ram': ram,
        'Weight': weight,
        'Touchscreen': touchscreen,
        'Ips': ips,
        'ppi': ppi,  # <- fixed lowercase
        'Cpu brand': cpu,
        'HDD': hdd,
        'SSD': ssd,
        'Gpu Brand': gpu,
        'os': os
    }])

    # Predict and show result
    prediction = np.exp(pipe.predict(query)[0])
    st.title(f"Predicted Price: ₹{int(prediction)}")
