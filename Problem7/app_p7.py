import streamlit as st
import string

def caesar_shift3(message):
    table = str.maketrans(string.ascii_uppercase[3:26]+string.ascii_uppercase[0:3], string.ascii_lowercase)
    return message.translate(table)

st.title("Problem 7 App")

# Get user input
user_message = st.text_input("Enter a plaintext message:")

if user_message:
  shifted_message = caesar_shift3(user_message)
  st.subheader("Encrypted message:")
  st.write(shifted_message)
