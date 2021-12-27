import re
import nltk

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()


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
    for shift in range(26):
        test_string = decrypt(encoded, shift)
        words = test_string.split()

        word_count = 0

        for word in words:
            word = re.sub(r"[^a-zA-Z]", "", word)
            if word.lower() in word_list or word in name_list:
                word_count += 1
        
        solution_score = int((word_count / len(words)) * 100)

        if solution_score > 90:
            return test_string
    
    return ''
