"""
@author: Nickolas Paternoster
@project: Algorithms Project 1
@file: encrypt_decrypt.py

This file is used for encrypting/decrypting
messages given a public and/or private key.

"""

# Used to convert ints to chars and store in array
def convertToChar(message):
    '''Converts a message to proper
    char values according to ASCII'''
    converted = []
    for value in message:
        converted.append(chr(value))
    return converted

def encrypt_recursive(m, e, n):
    ''' Returns m^e mod n = c '''
    if e == 0:
        return 1
    if e % 2 == 0:
        t = encrypt_recursive(m, e//2, n)
        return (t*t) % n
    else:
        t = encrypt_recursive(m, e//2, n)
        return m * (t**2 % n) % n

def decrypt_recursive(c, d, n):
    ''' Returns c^d mod n = m '''
    if d == 0:
        return 1
    if d % 2 == 0:
        t = decrypt_recursive(c, d // 2, n)
        return (t * t) % n
    else:
        t = decrypt_recursive(c, d // 2, n)
        return c * (t ** 2 % n) % n


# Takes a string and converts the characters to ascii values, then sends each of those values to the encryption method
def encrypt_string(str, e, n):
    '''Processes and encrypts a string'''
    string = list(str.encode('ascii'))
    encrypt = list()
    for i in string:
        encrypt.append(encrypt_recursive(i, e, n))
    return encrypt


# Runs encrypted ascii values and decrypts them with the private key
def decrypt_string(c, d, n):
    '''Processes and decrypts a string'''
    decrypt = list()
    for i in c:
        decrypt.append(decrypt_recursive(i, d, n))
    return decrypt

'''
# Used for testing the encryption / decryption on numbers and strings

# Message will go in index 0, e will go in 1, and n will go in 2

c = encrypt_string('testing', new_e, new_n)
print('Encrypted message is: ', c)

m = decrypt_string(c, new_d, new_n)
print('Decrypted message is: ', convertToChar(m))
'''