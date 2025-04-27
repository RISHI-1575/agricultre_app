import streamlit as st
from utils.auth_utils import validate_login, register_user

st.set_page_config(page_title="AgriPredict", layout="wide")

# Ensure session state is initialized
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None
if "current_page" not in st.session_state:
    st.session_state.current_page = "login"  # Default to login page

# Page Navigation Logic
def set_page(page_name):
    """
    Updates session state to navigate to the specified page.
    """
    st.session_state.current_page = page_name

# Restrict Access to Pages
if not st.session_state.logged_in:
    # Login and Sign-Up Page
    st.title("🌱 Welcome to AgriPredict")

    tab1, tab2 = st.tabs(["🔒 Login", "📝 Sign Up"])

    # Login Tab
    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        role = st.radio("Login as", ["farmer", "company"], key="login_role")

        if st.button("Login"):
            # Validate login using the `validate_login` function
            if validate_login(username, password, role):
                # Update session state and navigate to the main app
                st.session_state.logged_in = True
                st.session_state.role = role
                st.success("✅ Logged in successfully!")
                set_page("main")  # Navigate to the main page
            else:
                st.error("❌ Invalid credentials. Please check your username, password, and role.")

    # Sign-Up Tab
    with tab2:
        new_username = st.text_input("Choose a Username", key="signup_user")
        new_password = st.text_input("Choose a Password", type="password", key="signup_pass")
        new_role = st.radio("Register as", ["farmer", "company"], key="signup_role")

        if st.button("Sign Up"):
            # Register a new user using the `register_user` function
            message = register_user(new_username, new_password, new_role)
            if "🎉" in message:
                st.success(message)
            else:
                st.error(message)
else:
    # Main App Page (Post-Login)
    st.title("Welcome to AgriPredict!")
    st.markdown(f"👤 Logged in as **{st.session_state.role.capitalize()}**")

    # Main Navigation Buttons
    st.write("### Select a Feature to Get Started:")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Price Prediction"):
            set_page("price_prediction")
    with col2:
        if st.button("Crop Recommendation"):
            set_page("crop_recommendation")
    with col3:
        if st.button("Marketplace"):
            set_page("marketplace")

    # Main Content Based on Navigation
    if st.session_state.current_page == "price_prediction":
        from utils.price_prediction import price_prediction_page
        price_prediction_page()
    elif st.session_state.current_page == "crop_recommendation":
        from utils.crop_recommendation import crop_recommendation_page
        crop_recommendation_page()
    elif st.session_state.current_page == "marketplace":
        from utils.marketplace import marketplace_page
        marketplace_page()
