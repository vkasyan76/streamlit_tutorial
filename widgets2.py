import streamlit as st

# Initialize session state variables if they do not exist  

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False
    
if "user_input" not in st.session_state:  
    st.session_state.user_input = "" 

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox
    
st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input)

# in order to store the value, we need to write what we have in the state:
if st.session_state.checkbox:
    user_input = st.text_input("Enter something:", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")
    
st.write(f"User Input: {user_input}")