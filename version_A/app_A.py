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

# Ask the user for input
message = st.text_input("Enter your message: ")

# Encrypt using a +3 Caesar cipher
encrypted_message = caesar_cipher_encrypt(message, 3)

# Print the encrypted message
st.write("Encrypted message:", encrypted_message)
