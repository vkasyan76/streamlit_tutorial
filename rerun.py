import streamlit as st
import time

st.title("Counter Example with Immediate Rerun")

if "count" not in st.session_state:
    st.session_state.count = 0

def increment_and_rerun():
    st.session_state.count += 1
    st.rerun()

st.write(f"Current Count: {st.session_state.count}")

if st.button("Increment and Update Immediately"):
    increment_and_rerun()
