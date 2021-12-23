def encrypt(text, shift_num):
    encoded_string = ""

    for char in text:
        char_num = ord(char)

        if 65 <= char_num <= 90:
            shifted = ((char_num - 65) + shift_num) % 26
            char = chr(shifted + 65)
        elif 97 <= char_num <=122:
            shifted = ((char_num - 97) + shift_num) % 26
            char = chr(shifted + 97)
        
        encoded_string += char

    return encoded_string

def decrypt(encoded, shift_num):
    return encrypt(encoded, -shift_num)

def crack(encoded):
    pass