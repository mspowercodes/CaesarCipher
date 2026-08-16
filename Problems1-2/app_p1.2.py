import streamlit as st

def caesar_shift3(message):
  table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "DEFGHIJKLMNOPQRSTUVWXYZABC")
  return message.translate(table)

st.title("The App")

# Get user input
user_message = st.text_input("Enter a plaintext message:")

if user_message:
  shifted_message = caesar_shift3(user_message)
  st.subheader("Encrypted message:")
  st.write(shifted_message)
