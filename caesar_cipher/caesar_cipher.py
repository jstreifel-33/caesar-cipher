def encrypt(text, shift_num):
    encoded_string = ""

    for char in text:
        char_num = ord(char)

        if 65 <= char_num <= 90:
            origin = 65
        elif 97 <= char_num <=122:
            origin = 97
        
        shifted = ((char_num - origin) + shift_num) % 26
        char = chr(shifted + origin)

        encoded_string += char
    print(text, shift_num, encoded_string)
    return encoded_string

def decrypt(encoded, shift_num):
    pass

def crack(encoded):
    pass