
import streamlit as st
from utils.authentication import authenticate_user
from utils.home import home_page
from utils.price_prediction import price_prediction
from utils.crop_recommendation import crop_recommendation
from utils.marketplace import marketplace

# App title
st.set_page_config(page_title="Agriculture App", layout="wide")

# Login/Signup
st.sidebar.title("Login/Signup")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
role = st.sidebar.radio("Role", ["Farmer", "Company"])
login_button = st.sidebar.button("Login")

if login_button:
    if authenticate_user(username, password, role):
        st.sidebar.success(f"Welcome, {username}!")
        # Main navigation
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", ["Home", "Price Prediction", "Crop Recommendation", "Marketplace"])

        if page == "Home":
            home_page()
        elif page == "Price Prediction":
            price_prediction()
        elif page == "Crop Recommendation":
            crop_recommendation()
        elif page == "Marketplace":
            marketplace()
    else:
        st.sidebar.error("Invalid credentials. Please try again.")
