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

st.subheader("🔐 Version C: Choosing the shift")
st.write("This version lets you choose exactly how many spaces to shift your letters.")

# Added complexity: A slider widget for custom shift values
user_shift = st.slider("Choose your secret shift number:", min_value=1, max_value=25, value=3)

# Custom unique key for Version C input box
message = st.text_input("Enter your secret message:", key="cipher_input_c")

if message:
    # Check if the message is too long (keeping the rules from Version B)
    if len(message) > 20:
        st.error(f"❌ Too long! Your message has {len(message)} characters. Please keep it under 20.")
    else:
        # Encrypt using the student's chosen dynamic slider value
        encrypted_message = caesar_cipher_encrypt(message, user_shift)
        st.success(f"Encrypted message: {encrypted_message}")
        st.info(f"🔑 Using a +{user_shift} character shift")
