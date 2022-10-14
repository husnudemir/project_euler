"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
t = time.time()

def asal_sayilar(n):
    asal = [2]
    i = 3
    while i < n:
        for a in asal:
            if i % a == 0:
                break
        else:
            asal += [i]
        i += 1
    print(sum(asal))


asal_sayilar(2000000)

print(time.time()-t)