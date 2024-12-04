import streamlit as st
import pandas as pd
from datetime import datetime

min_date = datetime(1900,1,1)
max_date = datetime.now()

# Title
st.title("User Information Form")

# create Python dictionary to store values.

# form_values = {
#     "name": None,
#     "height": None,
#     "gender": None,
#     "dob": None,
# }



# Form to hold the interactive elements
# key is a unique form identifier
with st.form(key="user_info_form"):
    # Text Input
    # name = st.text_input("Enter your name: ")
    # age = st.number_input("Ener your age: ")
    # form_values["name"] = st.text_input("Enter your name: ")
    # form_values["height"]  = st.number_input("Ener your height (cm): ")
    # form_values["gender"]  = st.selectbox("Gender", ["Male","Female"])
    # form_values["dob"]  = st.date_input("Enter your birthdate", max_value=max_date, min_value=min_date)
    
    name1 = st.text_input("Enter your first name")
    birth_date = st.date_input("Enter your birth date", min_value=min_date, max_value=max_date)
    
    if birth_date:
        age = max_date.year - birth_date.year
        if birth_date.month > max_date.month or (birth_date.month == max_date.month and birth_date.day > max_date.day):
            age -=1
        st.write(f"Your calculated age is {age} years")
    
    submit_button1 = st.form_submit_button(label="Submit")
    if submit_button1:
        if not name1 or not birth_date:
            st.warning("Please fill in all of the fields")
        else:
            st.success(f"Thank you, {name1} Your age is {age}.")
            st.balloons()
            
    