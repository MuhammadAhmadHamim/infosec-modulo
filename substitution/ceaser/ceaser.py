"""
Caesar Cipher
=============

One of the oldest known ciphers, attributed to Julius Caesar. It is a
monoalphabetic substitution cipher: every letter of the plaintext is
replaced by the letter a fixed number of positions further along the
alphabet.

Terminology
-----------
Plaintext   the original, readable message
Cipher      the encrypted message (ciphertext)
Encryption  turning plaintext into cipher
Decryption  turning cipher back into plaintext

How it works
------------
Each letter is mapped to its position in the alphabet (A=0 ... Z=25),
shifted by the secret code, and wrapped around with modular arithmetic:

    Encryption:  E(x) = (x + code) mod 26
    Decryption:  D(x) = (x - code) mod 26

Example (code = 3):
    HELLO  ->  KHOOR   (and back again with decryption)

Key
---
The secret is the shift value ("hidden code"), an integer. The alphabet
string is passed in as `key`, so the cipher works on any ordered symbol
set, not only A-Z.

Functions
---------
encryption(key, m, code)      returns the cipher for message m
decryption(key, cipher, code) returns the original message

Limitations
-----------
Only 25 meaningful shifts exist, so the cipher falls to brute force
instantly, and letter frequencies pass through unchanged. It is for
learning only and offers no real security.
"""
key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(key, m, code):

    cipher = ''
    
    for ch in m:

        index = key.index(ch)
        
        index = (index + code) % len(key)

        cipher = cipher + key[index]

    return cipher

def decrypt(key, cipher, code):

    m = ''

    for ch in cipher:
        index = key.index(ch)
        index = (index - code) % len(key)

        m = m + key[index]

    return m

m = input('Enter your message:')

code = input('Enter the hidden code:')
code = int(code)

cipher = encrypt(key, m.upper(), code)

print('Cipher:', cipher)
print('Original:', decrypt(key, cipher, code))