import streamlit as st
from datetime import datetime

# A simple counter variable, without session state:
# Use session state NOT to immediately set to zero
# We update the sessio state not the variable
if "counter" not in st.session_state:
    # create key - value pair:
    st.session_state.counter = 0
    
st.write(f"Counter value: {st.session_state.counter}")

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
# else:
#     st.write(f"Counter did not reset")

# st.write(f"Counter value: {st.session_state.counter}")