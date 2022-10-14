"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time
t = time.time()

sayı = 20
i = 1
for k in range(1, sayı+1):
    for j in range(1, sayı+1):
        if (i*j) % k == 0:
            i *= j
            break
print(i)
print(time.time()-t)



"""
found = False
i = 20
while found==False:
    c = 0    # c checks if the number is the one im looking for
    for x in range(1,21):
        if i%x==0:
            c = c + 1
    if c==20: # if c = 20 then its the number im looking for
        print(i)
        found = True
    i = i + 1
print(time.time()-t)
"""

"""
from itertools import count
for i in count(20):
    if all(map(lambda x: i % x == 0, range(1, 21))):
        print(i)
        break
print(time.time()-t)
"""
