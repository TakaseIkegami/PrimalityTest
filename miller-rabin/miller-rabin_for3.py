# -*- coding: utf-8 -*-
import random

q = int(input('数値を入力して下さい(Input a number): '))

"""Miller-Rabin Primality Test"""
def primarity_test(q, k = 50):
    q = abs(q)

    if q == 2: return True
    if q < 2 or q & 1 == 0: return False

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, q-1)
        t = d
        y = pow(a, t, q)
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q-1 and t & 1 == 0:
            return False
    return True

if primarity_test(q) == True:
    print("素数だ…美しい…。(This is PRIME number.)")
if primarity_test(q) == False:
    print("素数じゃないよ><(This is NOT PRIME number.)")
    
