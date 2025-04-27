import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

def price_prediction():
    st.title("Crop Price Prediction")

    # Dropdowns for crop type and specific crop
    crop_type = st.selectbox("Select Crop Type", ["Vegetable", "Fruit"])
    crop = st.selectbox("Select Crop", ["Tomato", "Potato", "Apple", "Mango"])

    # Load prediction model
    try:
        model = pickle.load(open("models/price_prediction.pkl", "rb"))
        data = pd.read_csv("data/crop_prices.csv")
        
        # Predict prices and plot graph
        predicted_prices = model.predict(data)  # Dummy prediction
        st.line_chart(predicted_prices)
        
        # Option to download data
        st.download_button("Download Predicted Data", data.to_csv(index=False), file_name="predicted_prices.csv")
    except FileNotFoundError:
        st.error("Model or Data is missing!")
