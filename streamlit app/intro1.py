import streamlit as st

# Display a title
st.title("Hello, Streamlit!")

# Display some text
st.write("Welcome to your first Streamlit app!")

# Input from user
name = st.text_input("What's your name?")
st.write(f"Hello, {name}!")
