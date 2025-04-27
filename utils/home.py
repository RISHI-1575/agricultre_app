import streamlit as st
from utils.weather_api import get_weather
from utils.helpers import get_tips

def home_page():
    st.title("Home - Agriculture App")

    # Area Selection
    area = st.selectbox("Select Your Area", ["Karnataka"])

    # Fetch Weather
    weather = get_weather(area)
    st.write("### Weather Today:", weather)

    # Farming Tips
    tips = get_tips()
    st.write("### Farming Tips:", tips)
