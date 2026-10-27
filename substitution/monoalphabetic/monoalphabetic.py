"""
Monoalphabetic Substitution Cipher
==================================

A substitution cipher in which every plaintext letter is replaced by one
fixed, unique letter, using a single substitution alphabet for the whole
message. Caesar is the special case where that alphabet is just a shifted
copy of the original; here the cipher alphabet is an arbitrary
permutation of the 26 letters.

Terminology
-----------
Plaintext   the original, readable message
Cipher      the encrypted message (ciphertext)
Key         the cipher alphabet, a full permutation of the plain alphabet

How it works
------------
Two alphabets are lined up position by position:

    key1 (plain)   : abcdefghijklmnopqrstuvwxyz
    key2 (cipher)  : mzxkdbqgiphunwflvcaosrtyje

Encryption:  find the letter's position in key1, output the letter at
             that position in key2.
Decryption:  find the letter's position in key2, output the letter at
             that position in key1.

Example:
    a -> m, b -> z, c -> x    so    "abc"  ->  "mzx"

Key
---
The secret is key2. It must contain each of the 26 letters exactly once,
otherwise two plaintext letters would map to the same cipher letter and
decryption would become ambiguous.

Key space
---------
There are 26! (about 4 x 10^26) possible keys, far too many to brute
force, which is a big step up from Caesar's 25 shifts.

Functions
---------
encrypt(m, key2)   returns the cipher for the lowercase message m
decrypt(c)   returns the original message for the cipher c

Limitations
-----------
Each plaintext letter always becomes the same cipher letter, so the
letter frequencies of the language survive encryption. Frequency analysis
(e.g. 'e' being the most common English letter) breaks the cipher easily,
which motivates the polyalphabetic ciphers that follow. For learning
only; it offers no real security.
"""
import random
import string

def generate_key():
    """Method 1: shuffle the alphabet (fast, always a valid permutation)."""
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return ''.join(letters)

def generate_key_retry():
    """Method 2: draw random letters, rejecting repeats, until all 26 are used.
    Also returns the number of draws, to show how many get wasted."""
    k = ''
    attempts = 0

    while len(k) < 26:
        ch = chr(random.randint(97, 122))
        attempts += 1

        if ch not in k:
            k += ch

    return k, attempts

key1 = 'abcdefghijklmnopqrstuvwxyz'
key2 = 'mzxkdbqgiphunwflvcaosrtyje'

def encrypt(m, key2):
    result = ''

    for ch in m:
        index = key1.index(ch)

        result = result + key2[index]

    return result

def decrypt(c):
    result = ''

    for ch in c:
        index = key2.index(ch)

        result = result + key1[index]

    return result

message = input('Enter plain text:')

cipher = encrypt(message.lower(), key2)

print('Cipher:', cipher)
print('Decrypted message:', decrypt(cipher))