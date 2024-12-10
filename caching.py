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


# chache resource

# file_path = "example.tsx"

# # we can modify what is in the cache for every single user
# # instead of every user creating the file, the file object is created that every user shares

# @st.cache_resource
# def get_file_handler():
#     # Open the file in append mode, which cretes the file if it doesn't exist
#     file = open(file_path, "a+")
#     return file

# # Use the cashed file handler
# file_handler = get_file_handler()

# # Write to the file using the cashed handler
# if st.button("Write to File"):
#     file_handler.write("New line of text\n")
#     file_handler.flush() # Ensure the content iw written immediately
#     st.success("Wrote a new line to the file!")
    
# # Read and display the file contents
# if st.button("Read File"):
#     file_handler.seek(0)
#     content = file_handler.read()
#     st.text(content)
    
# # Always make sure to close the file when done (useful for resource cleanup)
# st.button("Close File", on_click=file_handler.close)


# Corrected code: 

# file_path = "example.txt"  
  
# @st.cache_resource  
# def get_file_handler():  
#     file = open(file_path, "a+")  
#     return file  
  
# def is_file_open(file):  
#     return not file.closed  
  
# file_handler = get_file_handler()  
  
# if st.button("Write to File"):  
#     if is_file_open(file_handler):  
#         file_handler.write("New line of text\n")  
#         file_handler.flush()  
#         st.success("Wrote a new line to the file!")  
#     else:  
#         st.error("File is closed. Please reload the app.")  
  
# if st.button("Read File"):  
#     if is_file_open(file_handler):  
#         file_handler.seek(0)  
#         content = file_handler.read()  
#         st.text(content)  
#     else:  
#         st.error("File is closed. Please reload the app.")  
  
# if st.button("Close File"):  
#     if is_file_open(file_handler):  
#         file_handler.close()  
#         st.success("File closed successfully!")  
#     else:  
#         st.warning("File is already closed.")  
        

# Corrected code 2: 

# st.experimental_rerun(): This function is called when an operation is attempted on a closed file. It will rerun the entire Streamlit script, effectively reinitializing all variables and cached resources, including reopening the file.
# Important Notes:
# State Reset: Using st.experimental_rerun() will reset the entire state of your app. If there are other stateful interactions in your app, they will also be reset.
# Streamlit Version: Ensure you are using an appropriate version of Streamlit that supports st.experimental_rerun() (this is available in Streamlit 0.65.0 and later).

file_path = "example.txt"  
  
@st.cache_resource  
def get_file_handler():  
    file = open(file_path, "a+")  
    return file  
  
def is_file_open(file):  
    return not file.closed  
  
file_handler = get_file_handler()  
  
if st.button("Write to File"):  
    if is_file_open(file_handler):  
        file_handler.write("New line of text\n")  
        file_handler.flush()  
        st.success("Wrote a new line to the file!")  
    else:  
        st.error("File is closed. Please reload the app.")  
        st.experimental_rerun()  # Rerun the app to reset the file handler  
  
if st.button("Read File"):  
    if is_file_open(file_handler):  
        file_handler.seek(0)  
        content = file_handler.read()  
        st.text(content)  
    else:  
        st.error("File is closed. Please reload the app.")  
        st.experimental_rerun()  # Rerun the app to reset the file handler  
  
if st.button("Close File"):  
    if is_file_open(file_handler):  
        file_handler.close()  
        st.success("File closed successfully!")  
    else:  
        st.warning("File is already closed.")  