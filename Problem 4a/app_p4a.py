import streamlit as st

def caesar_shift4(message):
  table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "EFGHIJKLMNOPQRSTUVWXYZABCD")
  return message.translate(table)

st.title("Problem 4a App")

# Get user input
user_message = st.text_input("Enter a plaintext message:")

if user_message:
  shifted_message = caesar_shift3(user_message)
  st.subheader("Encrypted message:")
  st.write(shifted_message)
