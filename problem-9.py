"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time
t = time.time()

for a in range(3,1000):
    for b in range(a+1, 999):
        kenarlar = (a ** 2) + (b ** 2)
        c = kenarlar ** 0.5
        if a + b + c == 1000:
            sonuc = a*b*c
            print(sonuc)
            print(a,b,c)
            break

print(time.time()-t)