import streamlit as st
from datetime import datetime

# to store step in the form that we are on:
if "step" not in st.session_state:
    st.session_state.step = 1
    
# to store personal infomation:
if "info" not in st.session_state:
    st.session_state.info = {}

# render part 1 of our form:   
if st.session_state.step == 1:
    st.header("Part 1: Info")
    # default is an empty string. manually set the value or make it equal to the session state:
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))
    
    # we move to the next step in our form:
    if st.button("Next"):
        st.session_state.info["name"] = name
        st.session_state.step  = 2

# render part 2 of our form: review updated name
# change elif to if
elif st.session_state.step == 2:
    st.header("Part 2: Review")
    
    st.subheader("Please review this:")
    st.write(f"**Name**: {st.session_state.info.get('name', '')}")

    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        
        st.session_state.info = {}
        
    if st.button("Back"):
        st.session_state.step = 1
        
        
