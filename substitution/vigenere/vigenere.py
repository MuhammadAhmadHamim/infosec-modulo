"""
Vigenère Cipher
===============

A polyalphabetic substitution cipher. Instead of one fixed shift for the
whole message (Caesar), a keyword supplies a different shift for each
letter, so the same plaintext letter can encrypt to different cipher
letters depending on its position.

This file implements the cipher two ways. Both use the same maths and
differ only in how the keyword is applied to the message.

Terminology
-----------
Plaintext   the original, readable message
Cipher      the encrypted message (ciphertext)
Code / Key  the secret keyword, repeated to cover the message

The maths (both methods)
------------------------
Letters become indexes (A=0 ... Z=25), the key letter is added to the
message letter, and the result wraps with mod 26:

    Encryption:  C[i] = (P[i] + K[i]) mod 26
    Decryption:  P[i] = (C[i] - K[i]) mod 26

Example (key = lemon):
    attackatdawn  ->  lxfopvefrnhr   (and back again with decryption)

Method 1: Counter-based, letters only
-------------------------------------
The message is converted to a list of indexes, spaces are skipped, and a
counter walks through the keyword, wrapping back to the start at the end.
Capital letters A-Z are used. Spaces are dropped from the cipher, so
decryption returns the message without spaces.

Functions: messageToIndexes(m), encrypt_method1(message_ints, code), decrypt_method1(cipher, code)

Method 2: Extended key, positions aligned
-----------------------------------------
The keyword is repeated until it is exactly as long as the message, so
each message position has its own key letter. Characters that are not
letters (spaces, digits, punctuation) are copied through unchanged, but
still use up one key letter. Lowercase letters a-z are used.

Functions: encrypt_method2(message, key), decrypt_method2(cipher, key)

How the methods differ
----------------------
For messages without spaces both methods give the same cipher. With
spaces they diverge:

    message "attack at dawn", key "lemon"
    Method 1:  lxfopvmhoeib       (spaces removed, key not advanced)
    Method 2:  lxfopv mh oeib     (spaces kept, key advances past them)

Key
---
The secret is the keyword: non-empty, letters only. A longer keyword
delays the repetition and is harder to break.

Limitations
-----------
Once the key length is found (Kasiski examination, index of
coincidence), the cipher reduces to several Caesar ciphers and falls to
frequency analysis. Method 1 loses spaces; Method 2 loses capitalisation.
For learning only; it offers no real security.
"""
def messageToIndexes(m):
    l = []

    for ch in m:
        if ord(ch) != 32:
            l.append(ord(ch) - 65)
        else:
            l.append(ord(ch))

    return l

def encrypt_method1(message_ints, code):
    c = ''

    counter = 0

    for i in message_ints:
        if i != 32:     # check for Space(' ')
            y = i + (ord(code[counter]) - 65)
            counter = (counter + 1) % len(code)
            z = y % 26
            c += chr(z + 65)
        else:
            continue

    return c

def decrypt_method1(cipher, code):
    m = ''

    counter = 0

    for ch in cipher:
        y = (ord(ch) - 65) - (ord(code[counter]) - 65)
        counter = (counter + 1) % len(code)
        y +=26
        z = y % 26
        m+= chr(z + 65)

    return m

def run_method1(m, code):

    key = messageToIndexes(m.upper())

    cipher_text = encrypt_method1(key, code)

    print('Cipher (method 1):', cipher_text)
    print('Decrypted cipher (method 1):', decrypt_method1(cipher_text, code))

def encrypt_method2(message, key):
    r = ''

    for i in range(len(message)):
        if message[i].isalpha():
            messageIndex = ord(message[i]) - ord('a')
            keyIndex = ord(key[i]) - ord('a')
            index = (messageIndex + keyIndex) % 26
            r = r + chr(index + ord('a'))
        else:
            r = r + message[i]
    
    return r

def decrypt_method2(cipher, key):
    r = ''

    for i in range(len(cipher)):
        if cipher[i].isalpha():
            cipherIndex = ord(cipher[i]) - ord('a')
            keyIndex = ord(key[i]) - ord('a')
            index = (cipherIndex - keyIndex) % 26
            r = r + chr(index + ord('a'))
        else:
            r = r + cipher[i]
    
    return r

def run_method2(message, key):

    if len(key) < len(message):

        counter = 0
    
        while len(key) != len(message):
            key = key + key[counter]
            counter = (counter + 1) % len(key)

    cipherText = encrypt_method2(message, key)
    originalMessage = decrypt_method2(cipherText, key)

    print('Cipher (method 2):', cipherText)
    print('Original Message (method 2):', originalMessage)

message = input('Enter your message:')
message = message.lower()

key = input('Enter your key:')

run_method1(message, key.upper())
run_method2(message, key.lower())