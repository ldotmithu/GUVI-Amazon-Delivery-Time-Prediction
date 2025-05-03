import streamlit as st
import numpy as np
import joblib, os
import pandas as pd
from datetime import datetime
import json


try:
    preprocessor = joblib.load("artifacts/data_transfomation/preprocess.pkl")
    model = joblib.load("artifacts/trainer/model.pkl")
    with open("artifacts/evaluation/metrics.json", 'r') as f:
        metrics = json.load(f)
    model_loaded = True
except:
    model_loaded = False


st.set_page_config(page_title="Amazon Delivery Time Predictor", page_icon="📦", layout="wide")
st.title("📦 Amazon Delivery Time Prediction")
st.markdown("Use the sidebar to fill in delivery details and predict delivery time (in minutes).")


with st.sidebar.expander("🛠️ Training Pipeline", expanded=False):
    if st.button("🚀 Run Full Training Pipeline"):
        with st.spinner("Running training pipeline. This may take a few minutes..."):
            os.system("python main.py")
            st.success("✅ Training pipeline completed successfully!")
            st.markdown('**Trained Model:** XGBoost')
            st.success(metrics)
            st.write("---")


st.sidebar.header("📥 Input Parameters")

with st.sidebar.expander("🧍 Agent Details", expanded=True):
    agent_age = st.slider("Agent Age", 18, 60, 30)
    agent_rating = st.slider("Agent Rating", 1.0, 5.0, 4.5, 0.1)

with st.sidebar.expander("📍 Location Details", expanded=True):
    store_lat = st.number_input("Store Latitude", value=6.9271)
    store_long = st.number_input("Store Longitude", value=79.8612)
    drop_lat = st.number_input("Drop Latitude", value=6.9219)
    drop_long = st.number_input("Drop Longitude", value=79.8651)

with st.sidebar.expander("🌤️ Environment & Vehicle", expanded=True):
    weather = st.selectbox("Weather Condition",['Sunny' 'Stormy' 'Sandstorms' 'Cloudy' 'Fog' 'Windy'])
    traffic = st.selectbox("Traffic Condition", ['High ' 'Jam ' 'Low ' 'Medium '])
    vehicle = st.selectbox("Vehicle Type", ['motorcycle ' 'scooter ' 'van'])
    area = st.selectbox("Delivery Area",  ['Urban ' 'Metropolitian ' 'Semi-Urban ' 'Other'])
    category = st.selectbox("Item Category",['Clothing' 'Electronics' 'Sports' 'Cosmetics' 'Toys' 'Snacks' 'Shoes'
 'Apparel' 'Jewelry' 'Outdoors' 'Grocery' 'Books' 'Kitchen' 'Home'
 'Pet Supplies' 'Skincare'])

with st.sidebar.expander("⏱️ Timing Details", expanded=True):
    order_date = st.date_input("Order Date", datetime.today())
    order_time = st.time_input("Order Time", datetime.now().time(), key="order_time")
    pickup_time = st.time_input("Pickup Time", datetime.now().time(), key="pickup_time")


if st.sidebar.button("🔮 Predict Delivery Time"):
    order_datetime = datetime.combine(order_date, order_time)
    pickup_datetime = datetime.combine(order_date, pickup_time)
    time_to_pickup = (pickup_datetime - order_datetime).total_seconds() / 60

    if time_to_pickup < 0:
        st.error("❗ Pickup time must be after order time.")
    else:
        order_hour = order_datetime.hour
        order_day = order_datetime.day
        order_month = order_datetime.month
        order_weekday = order_datetime.weekday()

        input_data = pd.DataFrame([{
            'Agent_Age': agent_age,
            'Agent_Rating': agent_rating,
            'Store_Latitude': abs(store_lat),
            'Store_Longitude': abs(store_long),
            'Drop_Latitude': drop_lat,
            'Drop_Longitude': drop_long,
            'Weather': weather,
            'Traffic': traffic,
            'Vehicle': vehicle,
            'Area': area,
            'Category': category,
            'Time_to_Pickup': time_to_pickup,
            'Order_Hour': order_hour,
            'Order_Day': order_day,
            'Order_Month': order_month,
            'Order_Weekday': order_weekday
        }])

        transformed_data = preprocessor.transform(input_data)
        prediction = model.predict(transformed_data)

        st.markdown("---")
        st.subheader("📋 Input Summary")
        st.dataframe(input_data)

        st.subheader("📦 Predicted Delivery Time")
        st.success(f"⏱️ Estimated Delivery Time: **{prediction[0]:.2f} minutes**")
