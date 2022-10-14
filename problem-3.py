"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
asal çarpan 
"""

import time
t = time.time()

def asal_mi(sayı):
    if sayı == 1:
        return False
    elif sayı == 2:
        return True
    else:
        for i in range(2, sayı):
            if sayı % i == 0:
                return False
        return True


sayi = 600851475143

for i in range(1, sayi):
    if sayi % i == 0:
        if asal_mi(i):
            print(i)
            if i == 6857:
                break

print(time.time()-t)