import streamlit as st
import os

# st.write("Hello World")
# st.write({"key": "value"})
# st.write(123)
# 3 * 4
# "hello world" if False else "bye"

# pressed = st.button("Press me")
# print('First', pressed)

# pressed2 = st.button("Second Button")
# print('Second', pressed2)

st.title("Super Simple Title")
st.header("This is a header")
st.subheader("Subheader")
st.markdown("This is **Markdown**")
st.markdown("This is _Markdown_")
st.caption("small text")
code_example = """
def greet(name):
    print('hello', name)
"""
st.code(code_example, language="python")
st.divider()

# put images on the screen
st.image(os.path.join(os.getcwd(), "static", "GEN AI -unsplash.jpg"))

