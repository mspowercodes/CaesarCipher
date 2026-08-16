import streamlit as st


def caesar_shift3(message):
  # Shift letters by 3 positions
  table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "DEFGHIJKLMNOPQRSTUVWXYZABC")
  return message.translate(table)


st.title("Caesar Cipher App")

# Get user input
user_message = st.text_input("Enter a message to shift:")

if user_message:
  shifted_message = caesar_shift3(user_message)
  st.subheader("Shifted Result:")
  st.write(shifted_message)
