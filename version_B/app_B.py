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

st.subheader("🚀 Version B: Limiting message length")
st.write("This version adds a rule: your secret message cannot be longer than 20 characters!")

# Custom unique key for Version B input box
message = st.text_input("Enter your secret message:", key="cipher_input_b")

if message:
    # Check if the message is too long
    if len(message) > 20:
        st.error(f"❌ Too long! Your message has {len(message)} characters. Please keep it under 20.")
    else:
        # If it passes the check, encrypt it normally
        encrypted_message = caesar_cipher_encrypt(message, 3)
        st.success(f"Encrypted message: {encrypted_message}")
        st.info(f"📏 Message length: {len(message)} / 20 characters")
