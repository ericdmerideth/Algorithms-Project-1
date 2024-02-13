# -*- coding: utf-8 -*-

import math
import random

def gen_prime(n1, n2):
    '''Generates pseudo-primes using Fermat's theorem with edge case protection and input adjustment.'''
    # Adjust if n2 is less than n1
    if n2 < n1:
        n1, n2 = n2, n1  # Swap values to ensure n1 is always less than n2

    attempts = 0
    max_attempts = 10000  # Set a limit to prevent infinite loops
    while True:
        if attempts >= max_attempts:
            raise Exception("Unable to find a prime number within the specified range after numerous attempts.")
        attempts += 1

        pseudo_prime = True
        p = random.randint(n1, n2)
        for i in range(50):  # According to research, a k-value of 50 is effective
            j = random.randint(2, p-2)  # Adjusted to avoid potential edge cases with j=1 or j=p-1
            if pow(j, p-1, p) != 1:
                pseudo_prime = False
                break
        if pseudo_prime:
            return p

def ext_gcd(a, b):
    '''
    Computes triplet x,y,d such that 
    d = gcd(a,b) = ax + by.
    We use this to find the multiplicative inverse for private key d.
    '''
    if b == 0:
        return (1, 0, a)
    (x, y, d) = ext_gcd(b, a%b)
    return y, x - a//b*y, d # x and y shift, d drops down
   
    
def RSA_gen_keys(n1, n2):# Upper and lower bounds for primes
    p = q = n = e = d = phi = trpl = 0    

    # Generate and validate large primes p and q    
    pq_equal = True
    while pq_equal:
        p = gen_prime(n1, n2)
        q = gen_prime(n1, n2)
        if p != q: break
        
    # Calculate n and phi
    n = p * q
    phi = (p-1) * (q-1)
    
    # Find e in ring phi relatively prime to phi
    while True:
        e = random.randint(n1, n2)
        if (math.gcd(e,phi) == 1):
            break
    
    # Find d in ring phi, the multiplicative inverse of e
    result = ext_gcd(e, phi)
    d = result[0] % phi # The private key is our final x-value, mod phi
    
    # Returning variables
    return (p, q, n, e, d, phi)
    
    



