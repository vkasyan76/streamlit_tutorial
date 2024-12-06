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
    
# Columns layout
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")
    
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")

# Containers example
with st.container(border=True):
    st.write("This is inside a container")
    st.write("You can think of containers as a grouping for elements")
    st.write("Containers help manage sections of the page")

# Empty placeholder
placeholder = st.empty()
placeholder.write("This is an empty placeholder, usefull for dynamic content.")

if st.button("Update Placeholder"):
    placeholder.write("The content of this placeholder has been updated.")
    
# Expander
with st.expander("Expand for more details"):
    st.write("This is additional information that is hidden by default.")
    st.write("You can use expanders to keep your interface cleaner")

# Popover (Tooltip)
st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooltip or popover or hover.")

#Sidebar input handling
if sidebar_input:
    st.write(f"You entered in the sidebar: {sidebar_input}")

    