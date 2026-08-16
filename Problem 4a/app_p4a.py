import streamlit as st

def caesar_shift4(message):
  table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "EFGHIJKLMNOPQRSTUVWXYZABCD")
  return message.translate(table)

st.title("Caesar Cipher App")

# Get user input
user_message = st.text_input("Enter a message to shift:")

if user_message:
  shifted_message = caesar_shift4(user_message)
  st.subheader("Shifted Result:")
  st.write(shifted_message)
