"""
Vigenère Cipher
===============

A polyalphabetic substitution cipher. Instead of one fixed shift for the
whole message (Caesar), a keyword supplies a different shift for each
letter, so the same plaintext letter can encrypt to different cipher
letters depending on its position.

Terminology
-----------
Plaintext   the original, readable message
Cipher      the encrypted message (ciphertext)
Code        the secret keyword, repeated to cover the message length

How it works
------------
Letters are converted to indexes (A=0 ... Z=25) by subtracting 65 from
their ASCII value. Each message letter is shifted by the matching letter
of the code, wrapping around with mod 26. The code is reused cyclically
(a counter moves through it and resets at the end).

    Encryption:  C[i] = (P[i] + K[i mod len(K)]) mod 26
    Decryption:  P[i] = (C[i] - K[i mod len(K)]) mod 26

For decryption the subtraction can go negative, so 26 is added before the
modulus. This does not change the result, since the modulus removes it
again, but it keeps the value non-negative.
The index is finally converted back to a letter by adding 65 (capitals).

Example (code = LEMON):
    ATTACKATDAWN  ->  LXFOPVEFRNHR   (and back again with decryption)

Key
---
The secret is the keyword. A longer keyword gives more shifts before the
pattern repeats, which makes the cipher harder to break than Caesar.

Functions
---------
encrypt(message_ints, code)   returns the cipher for the message
                                (given as a list of letter indexes)
decrypt(cipher, code)         returns the original message for the cipher
messageToIndexes(m)       converts a message into the list of indexes
                            that encrypt() expects

Limitations
-----------
Spaces are skipped during encryption, so decryption returns the message
without spaces. Only capital letters A-Z are supported. Because the code
repeats, the cipher is vulnerable to Kasiski examination and
index-of-coincidence analysis once the key length is found. For learning
only; it offers no real security.
"""
def messageToIndexes(m):
    l = []

    for ch in m:
        if ord(ch) != 32:
            l.append(ord(ch) - 65)
        else:
            l.append(ord(ch))

    return l

def encrypt(message_ints, code):
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

def decrypt(cipher, code):
    m = ''

    counter = 0

    for ch in cipher:
        y = (ord(ch) - 65) - (ord(code[counter]) - 65)
        counter = (counter + 1) % len(code)
        y +=26
        z = y % 26
        m+= chr(z + 65)

    return m

m = input('Enter any message:')
code = input('Enter the code:')

code = code.upper()

key = messageToIndexes(m.upper())

cipher_text = encrypt(key, code)

print('Cipher:', cipher_text)
print('Decrypted cipher:', decrypt(cipher_text, code))