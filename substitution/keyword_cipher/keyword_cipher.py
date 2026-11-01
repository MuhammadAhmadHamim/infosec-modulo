"""
Keyword Cipher
==============

A monoalphabetic substitution cipher whose cipher alphabet is built from
a secret keyword. Instead of storing a random permutation of the
alphabet (as in the plain monoalphabetic cipher), the key is generated
from an easy-to-remember word, which makes it practical to share and
reproduce.

Terminology
-----------
Plaintext   the original, readable message
Cipher      the encrypted message (ciphertext)
Code        the secret keyword the key is built from
Key         the cipher alphabet derived from the code

How it works
------------
1. Take the code and remove repeated letters, keeping the first
   occurrence of each.
2. Append every remaining letter of the alphabet in normal order.
3. The result is a full 26-letter cipher alphabet, lined up against the
   plain alphabet position by position.

Example (code = hello):
    unique letters : helo
    key            : heloabcdfgijkmnpqrstuvwxyz
    plain          : abcdefghijklmnopqrstuvwxyz

    Encryption:  find the letter's position in the plain alphabet,
                 output the letter at that position in the key.
    Decryption:  find the letter's position in the key,
                 output the letter at that position in the plain
                 alphabet.

    "hello"  ->  "dajjn"   (and back again with decryption)

Key
---
The secret is the code. Anyone who knows it can rebuild the exact key.
The code should contain letters only, since any other character would
end up inside the key and break the one-to-one mapping.

Functions
---------
build_key(code)       builds and returns the key from the code
encrypt(m, key)      returns the cipher for the lowercase message m
decrypt(c, key)      returns the original message for the cipher c

Limitations
-----------
Each plaintext letter always maps to the same cipher letter, so letter
frequencies survive encryption and frequency analysis breaks it. The
key is also weaker than a random permutation: the tail of the key is
just the alphabet in order, and short or common keywords are easy to
guess. Spaces and punctuation are not supported. For learning only; it
offers no real security.
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def build_key(code):
    pure_code = ''

    for ch in code:
        if ch not in pure_code:
            pure_code += ch

    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in pure_code:
            pure_code += chr(i)

    return pure_code

def encrypt(m, key):
    r = ''

    for ch in m:
        i = alphabet.index(ch)

        r = r + key[i]

    return r

def decrypt(c, key):
    r = ''

    for ch in c:
        i = key.index(ch)

        r = r + alphabet[i]

    return r

code = input('Enter your code:')
key = build_key(code.lower())
print('Key:', key)

message = input('Enter plain text:')
cipher = encrypt(message.lower(), key)

print('Cipher:', cipher)
print('Decrypted message:', decrypt(cipher, key))