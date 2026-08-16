def caesar_shift3(message):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "DEFGHIJKLMNOPQRSTUVWXYZABC")
    return message.translate(table)
