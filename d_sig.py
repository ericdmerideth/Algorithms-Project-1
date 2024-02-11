"""
Algorithms I
Eric Merideth Jake Speets

This file is used for signing and
authenticating digital signatures.

"""

import e_d_crypt
import k_gen

def fastExpo_recursive(a, p, n):
    ''' Returns a^p mod n '''
    if p == 0:
        return 1
    if p%2 == 0:
        t = fastExpo_recursive(a, p//2, n)
        return (t*t)%n
    else:
        t = fastExpo_recursive(a, p//2, n)
        return a *(t**2%n)%n

def sign(m, n, d):
    '''Creates a digital signature'''
    s = list()
    for i in m:
        s.append(fastExpo_recursive(i, d, n))
    return s

def authenticate(s, n, e):
    '''Authenticates a digital signature'''
    m = list()
    for i in s:
        m.append(fastExpo_recursive(i, e, n))
    return m