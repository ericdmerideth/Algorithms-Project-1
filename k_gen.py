"""
@author: Shandon Probst
@project: Algorithms Project 1
@file: key_gen.py

This file is used for RSA key generation. Firstly, we generate
two pseudo primes (p and q) using Fermat's algortihm. Secondly,
we find an e relatively prime to phi N = (p-1)(q-1). Third, we
find d, which is the multiplicative inverse of e in Z sub phi.

"""
import random

# Global values for use in other files
global p_perm
global q_perm
global n_perm
global e_perm
global d_perm
global phiN_perm


def generateRandomPrime(min_size, max_size):
    ''' Returns a random prime number'''
    while True:
        randomPrime = random.randrange(min_size, max_size)
        if (Fermat(randomPrime)):
            return randomPrime


def coPrime(a, b):
    ''' Determines if gcd(a,b) is 1 (relatively prime)'''
    return egcd(a, b) == 1


def Fermat(randomPrime):
    ''' Test if number is prime with Fermat's little theorem'''
    t = True
    for i in range(1, randomPrime):
        if pow(i, randomPrime - 1, randomPrime) != 1:
            t = False
            break
    return t


# Finds the GCD of two numbers
def egcd(a, b):
    ''' The gcd function implements Euclid's
    GCD algorithm to find the greatest common
    divisor of two positive integers a and b'''

    if b == 0:
        return a
    else:
        return egcd(b, a % b)


# Finds the multiplicative inverse
def extended_egcd(a, b):
    ''' The extended_gcd function implements the
    extension of Euclid's GCD algorithm to find integers x and y
    such that ax + by = gcd(a, b) '''
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_egcd(b, a % b)
    return y, x - a // b * y, d


def generateKeys(min_size, max_size):
    ''' Function that generates RSA keys within given range'''
    p = q = e = d = n = 0

    # Generates a random prime number for p and q
    p = generateRandomPrime(min_size, max_size)  # prime number p
    q = generateRandomPrime(min_size, max_size)  # prime number q

    # Prevents q from equaling the same value as p
    while (q == p):
        q = generateRandomPrime(min_size, max_size)
        if (q != p):
            break

    # Calculate n and phi N
    n = p * q
    phiN = (p - 1) * (q - 1)  # phi N

    # Calculate e, where e is relatively prime with phi N
    while True:
        e = random.randrange(min_size, max_size)
        if (coPrime(e, phiN)):
            break

    # Calculate d, the modular multiplicative inverse
    d = extended_egcd(e, phiN)
    d = d[0]
    if d < 1:
        d = phiN + d

    # Global variables defined
    global p_perm
    p_perm = p
    global q_perm
    q_perm = q
    global n_perm
    n_perm = n
    global e_perm
    e_perm = e
    global d_perm
    d_perm = d
    global phiN_perm
    phiN_perm = phiN


# This chunk allows you to test the key generation and get output values
'''
    print('p is:' , p)
    print('q is:' , q)
    print('n is:' , n)
    print('phiN is:' , phiN)
    print('e is:' , e)
    print('d is:' , d)

generateKeys(100000, 1000000)
'''