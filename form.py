import streamlit as st
import pandas as pd
from datetime import datetime

# Title
st.title("User Information Form")

# create Python dictionary to store values.

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None,
}

min_date = datetime(1900,1,1)
max_date = datetime.now()

# Form to hold the interactive elements
# key is a unique form identifier
with st.form(key="user_info_form"):
    # Text Input
    # name = st.text_input("Enter your name: ")
    # age = st.number_input("Ener your age: ")
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"]  = st.number_input("Ener your height (cm): ")
    form_values["gender"]  = st.selectbox("Gender", ["Male","Female"])
    form_values["dob"]  = st.date_input("Enter your birthdate", max_value=max_date, min_value=min_date)
    
    # print(name, age)
    
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")
            
    