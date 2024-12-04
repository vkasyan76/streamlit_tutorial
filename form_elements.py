import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Form Demo")

# Form to hold the interactive elements
# key is a unique form identifier
with st.form(key="user_info_form"):
    # Text Input
    st.subheader("Text Inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide your feedback")
    
    # Date and Time Inputs
    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Choose a preferred time")
    
    # Selectors
    st.subheader("Selectors")
    choice = st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3'])
    gender = st.selectbox("Select your gender", ['Male', 'Female', 'Other'])
    slider_value = st.select_slider("Select a range", options=[1,2,3,4,5])
    
    # Toggles and Checkboxes
    st.subheader("Toggles and Checkboxes")
    notifications = st.checkbox("Receive notifications?")
    toggle_value = st.checkbox("Enable dark mode?", value=False)
    
    
    # Submit Button for the Form
    submit_button = st.form_submit_button(label="Submit")

# Outside of the form 
st.subheader("Buttons")
