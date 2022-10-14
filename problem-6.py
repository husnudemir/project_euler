"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
t1 = 0
for i in range(101):
    i **= 2
    t1 += i

t2 = 0
for i in range(101):
    t2 += i

print(t2 ** 2 - t1)

