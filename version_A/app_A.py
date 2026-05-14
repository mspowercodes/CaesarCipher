import streamlit as st

# Define the helper function for encryption
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

st.subheader("🔐 Version A: The +3 cipher")
st.write("This version takes your message and shifts every letter by 3 spaces")

# Custom unique key for the input box
message = st.text_input("Enter your secret message:", key="cipher_input_a")

if message:
    # Encrypt using a +3 Caesar cipher
    encrypted_message = caesar_cipher_encrypt(message, 3)
    
    # Display the result to the student
    st.success(f"Encrypted message: {encrypted_message}")
