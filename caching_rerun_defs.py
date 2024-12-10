import streamlit as st
import time

# to have slow applications not constantly re-run
#cache data is used wehn we have immmutable data (always the same)
# in below case - we return a dictionary

@st.cache_data(ttl=60) # Cache this data for 60 seconds
def fetch_data():
    # Simulate a slow data-fetching process
    time.sleep(3) # Delays to mimic an API call
    return {"data": "This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)
   

# Corrected code 3: 

# st.experimental_rerun(): This function is called when an operation is attempted on a closed file. It will rerun the entire Streamlit script, effectively reinitializing all variables and cached resources, including reopening the file.
# Important Notes:
# State Reset: Using st.experimental_rerun() will reset the entire state of your app. If there are other stateful interactions in your app, they will also be reset.
# Streamlit Version: Ensure you are using an appropriate version of Streamlit that supports st.experimental_rerun() (this is available in Streamlit 0.65.0 and later).


# You can utilize Streamlit's session state to manage the file handler, ensuring that it is properly initialized after each rerun.

# open_file() Function: This function ensures that the file is opened if it's not already open or if it was previously closed. It updates the file_handler in the session state.
# Reopen on Button Press: Each button press first calls open_file() to ensure that the file is open before attempting any operations. This handles the case where the file might be closed, ensuring that operations can be performed consistently.
# Checking File State: The is_file_open() function checks if the file is open, and the logic is streamlined to ensure the file's state is managed correctly across different interactions.

file_path = "example.txt"  
  
def open_file():  
    """Open the file in append mode and store the file handler in session state."""  
    if 'file_handler' not in st.session_state or st.session_state.file_handler.closed:  
        st.session_state.file_handler = open(file_path, "a+")  
    return st.session_state.file_handler  
  
def is_file_open(file):  
    """Check if a file is open."""  
    return not file.closed  
  
# Ensure the file is open at the start  
file_handler = open_file()  
  
if st.button("Write to File"):  
    file_handler = open_file()  # Reopen the file if needed  
    if is_file_open(file_handler):  
        file_handler.write("New line of text\n")  
        file_handler.flush()  
        st.success("Wrote a new line to the file!")  
    else:  
        st.error("File is closed. Please reload the app.")  
  
if st.button("Read File"):  
    file_handler = open_file()  # Reopen the file if needed  
    if is_file_open(file_handler):  
        file_handler.seek(0)  
        content = file_handler.read()  
        st.text(content)  
    else:  
        st.error("File is closed. Please reload the app.")  
  
if st.button("Close File"):  
    if is_file_open(file_handler):  
        file_handler.close()  
        st.success("File closed successfully!")  
    else:  
        st.warning("File is already closed.")  