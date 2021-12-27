# Encryption and the Caesar Cipher

An exercise in encryption and cracking using the **Caesar cipher**.

The Caesar cipher is one of the oldest known encryption methods. It involves shifting the letters of an alphabet by a known number of letters to encrypt a message via substitution.

## API

* `encrypt(string, shift_num)` - Accepts a phrase composed of English characters as a string and a number of characters to shift by. Returns the encrypted phrase as a string.
* `decrypt(encoded_string, shift_num)` - Accepts an encrypted phrase as a string and a number representing the shift used for encryption. Returns the decrypted phrase as a string.
* `encrypt(encoded_string)` - Accepts an encrypted English phrase. Uses brute force to decrypt the phrase based on word and name analysis. Returns the decrypted phrase as a string or an empty string if decryption is not possible.

## Deployment

App is not deployed to any server or website. To use, please feel free to fork or clone the project yourself!

App is build using Poetry and has the following dependencies:

* `nltk` - Natural Language Toolkit for Python

## Submission

[working branch #1](https://github.com/jstreifel-33/caesar-cipher/pull/1)
