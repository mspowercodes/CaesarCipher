import streamlit as st
import string

# Get user input
shift = st.number_input(“Enter the shift amount:”)

def caesar_shift_user(message):
    table = str.maketrans(string.ascii_lowercase, string.ascii_uppercase[shift:26]+string.ascii_uppercase[0:shift])
    return message.translate(table)

st.title("Problem 5e App")

# Get user input
user_message = st.text_input("Enter a plaintext message:")

if user_message:
  shifted_message = caesar_shift_user(user_message)
  st.subheader("Encrypted message:")
  st.write(shifted_message)
