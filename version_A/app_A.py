import streamlit as st

st.subheader("🤖 Version A: The Basics")
st.write("This is a simple app that greets you.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
