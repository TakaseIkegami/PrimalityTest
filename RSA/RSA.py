#__author__ = 'upupu_000.CROLERA'
#coding:utf8
import random

"""Miller-Rabin primality test"""
def primarity_test(q, k = 50):
    q = abs(q)

    if q == 2: 
        return True
    if q < 2 or q & 1 == 0:
        return False

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in xrange(k):
        a = random.randint(1, q - 1)
        t = d
        y = pow(a, t, q)
        while t != q - 1 and y != 1 and y != q - 1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q -1 and t & 1 == 0:
            return False
    return True

"""Generate any bit prime number"""
def generate_prime(bit):
    if bit < 3:
        raise ValueError,'"2" and "3" are so vulnerable, that must be large than 2bit.'

    min_i = 1 << (bit - 1)
    max_i = (mini_i << 1) - 1
    while True:
        if is_prime():
            break
        x = x + 1
        if x + 1 <= max_i else min_i
        return x

def generate_pq(bit):
    min_i = 1 << (bit - 1)
    max_i = (min_i << 1) - 1
    while True:
        t = random.randint(3, bit - 3)
        p = genarate_prime(t)
        q = generate_prime(bit - t)
        if min_i < (p * q) < max_i:
            break
        return (p, q)

"""Greatest common divisor"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

"""Least common multiple"""
def lcm(a, b):
    return a * b / gcd(a, b)

"""Euclidean algorithm"""
def ea(a, b):
    if b == 0:
        u = 1
        v = 0
    else:
        q = a / b
        r = a % b
        (u0, v0) = eu(b, r)
        u = v0
        v = u0 - q* v0
    return (c, v)



