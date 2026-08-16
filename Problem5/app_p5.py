import string

def caesar_shift3(message):
    table = str.maketrans(string.ascii_lowercase, string.ascii_uppercase)
    return message.translate(table)
