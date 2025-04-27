import streamlit as st
import pandas as pd

def marketplace():
    st.title("Marketplace")

    # Form for companies to post requirements
    st.write("### Post a Requirement (Companies)")
    if st.button("Submit"):
        st.success("Requirement posted successfully!")

    # Farmers can view requirements
    st.write("### View Requirements")
    try:
        requirements = pd.read_csv("data/marketplace.csv")
        st.table(requirements)
    except FileNotFoundError:
        st.error("No requirements to show!")
