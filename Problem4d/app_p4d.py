import streamlit as st

def caesar_shift4decrypt(message):
  table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "wxyzabcdefghijklmnopqrstuv")
  return message.translate(table)

st.title("Problem 4d App")

# Get user input
user_message = st.text_input("Enter a ciphertext message:")

if user_message:
  shifted_message = caesar_shift4decrypt(user_message)
  st.subheader("Decrypted message:")
  st.write(shifted_message)
