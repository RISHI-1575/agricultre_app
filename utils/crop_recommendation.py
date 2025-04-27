import streamlit as st
import pandas as pd
import pickle

def crop_recommendation():
    st.title("Crop Recommendation")

    # Input for land size
    land_size = st.number_input("Enter Your Land Size (in acres)", min_value=1)

    # Load recommendation model
    try:
        model = pickle.load(open("models/crop_recommendation.pkl", "rb"))
        data = pd.read_csv("data/crop_recommendation.csv")
        
        # Get recommendations and display as a table
        recommended_crops = model.predict(data)  # Dummy recommendation
        st.table(recommended_crops)
        
        # Option to download recommendations
        st.download_button("Download Recommendations", data.to_csv(index=False), file_name="crop_recommendations.csv")
    except FileNotFoundError:
        st.error("Model or Data is missing!")
