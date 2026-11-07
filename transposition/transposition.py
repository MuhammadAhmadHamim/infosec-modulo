"""
Transposition Cipher (Token-Based)
==================================

A transposition cipher: no letter is changed, only moved. The message is
cut into fixed-size tokens, stacked into a matrix, and the columns are
read out in a secret order.

Terminology
-----------
Plaintext   the original, readable message
Cipher      the encrypted message (ciphertext)
Token       a fixed-size chunk of the message (one row of the matrix)
Key         the column order the matrix is read in

How it works
------------
1. Split the message into tokens of size s. If the last token is
   short, pad it with spaces so every row has exactly s characters.
2. Stack the tokens as rows of a matrix.
3. The key is a permutation of the column numbers 0 .. s-1.
4. Encryption reads the matrix column by column in key order.
   Decryption writes the cipher back into the columns in key order,
   then reads the matrix row by row.

Example (token size = 4, key = 2 0 3 1):
    matrix:   A T T A
              C K A T
              D A W N

    columns read in order 2, 0, 3, 1:  TAW + ACD + ATN + TKA

    "ATTACKATDAWN"  ->  "TAWACDATNTKA"  (and back again with decryption)

Key
---
The secret is the token size together with the column order. Both are
needed for decryption, and the order must use every column exactly once.

Functions
---------
matrix_formation(m, s)         splits the message into padded tokens
create_key(s)                  asks for the column order and returns it
encrypt(m, s, col_list)        returns the cipher for message m
decrypt(cipher, s, col_list)   returns the original message for the cipher

Limitations
-----------
Letters are only rearranged, so letter frequencies are unchanged, which
gives a cryptanalyst a strong hint that a transposition was used.
Padding spaces are added to short messages and stripped on decryption,
so genuine trailing spaces in the original are lost. For learning only;
it offers no real security.
"""
def matrix_formation(m, s):
    matrix = [] 

    for i in range(0,  len(m),  s):  
        token = m[i: i + s]

        if len(token) != s:
            while len(token) != s:
                token+= ' '

        matrix.append(token)

    return matrix

def create_key(s):
    col_list = []

    while len(col_list) < s:
        n = int(input('Enter the sequence number of column:'))

        if n < 0 or n >= s:
            print('Index not in range!')
        elif n in col_list:
            print('No repetition allowed!')
        else:
            col_list.append(n)

    return col_list

def encrypt(m, s, col_list):
    # Calling the matrix_formation function to get the values in matrix
    matrix = matrix_formation(m, s)

    cipher = ''

    for j in col_list:
        for i in range(len(matrix)):
            cipher += matrix[i][j]

    return cipher

def decrypt(cipher, s, col_list):
    rows = len(cipher) // s

    matrix = []
    for i in range(rows):
        matrix.append([''] * s)

    pos = 0
    for j in col_list:
        for i in range(rows):
            matrix[i][j] = cipher[pos]
            pos += 1

    m = ''
    for i in range(rows):
        for j in range(s):
            m += matrix[i][j]

    return m.rstrip()

m = input('Enter any string:') # Message

s = input('Enter the size of token:') # Size of token
s = int(s)

# Calling the create_keys function to get the sequence of columns
col_list = create_key(s)

cipher = encrypt(m, s, col_list)

print('Cipher:', cipher)
print('Decrypted message:', decrypt(cipher, s, col_list))