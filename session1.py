import streamlit as st
from datetime import datetime

# A simple counter variable, without session state:
# On re-run immediately set to zero
counter = 0

st.write(f"Counter value: {counter}")

# Button to increment the counter
if st.button("Increment Counter"):
    counter += 1
    st.write(f"Counter incremented to {counter}")
else:
    st.write(f"Counter stays at {counter}")