import streamlit as st

# Updated dual-purpose algorithm for encryption/decryption
def caesar_cipher_encrypt_decrypt(text, shift, mode='encrypt'):
    result_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
        elif 'A' <= char <= 'Z':
            start = ord('A')
        else:
            result_text += char
            continue
            
        if mode == 'decrypt':
            shifted_char_code = (ord(char) - start - shift + 26) % 26 + start
        else: # encrypt
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            
        result_text += chr(shifted_char_code)
    return result_text

st.subheader("🚀 Version D: Encrypt or decrypt")
st.write("This version adds full decryption and updates the length limit to 250 characters.")

# UI controls automatically enforce valid choices without needing input error loops
mode_choice = st.selectbox("What action do you want to perform?", ["encrypt", "decrypt"], key="mode_d")
user_shift = st.slider("Choose your secret shift number:", min_value=1, max_value=25, value=3, key="shift_d")

message = st.text_input("Enter your message:", key="cipher_input_d")

if message:
    # Handle the length constraint cleanly in the UI
    if len(message) > 250:
        st.warning(f"⚠️ Truncated! Your message was too long. We clipped it from {len(message)} down to 250 characters.")
        message = message[:250]
        
    # Process the text using the dynamic UI choices
    processed_message = caesar_cipher_encrypt_decrypt(message, user_shift, mode_choice)
    
    # Display the final output with a clean indicator badge
    st.success(f"✨ {mode_choice.capitalize()}ed result: {processed_message}")
    st.info(f"📏 Final tracking length: {len(message)} / 250 characters")
