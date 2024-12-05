import streamlit as st

# Sidebar layout
st.sidebar.title("This is the Sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and text here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")


# Tabs layout
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1: 
    st.write("You are in tab 1")
with tab2: 
    st.write("You are in tab 2")
with tab3: 
    st.write("You are in tab 3")