"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
10'in altında 3 veya 5'in katları olan tüm doğal sayıları listelersek 3, 5, 6 ve 9 rakamlarına ulaşırız. Bu katların toplamı 23'dir.

3 veya 5'in tüm katlarının toplamını 1000'den aşağıda bulabilirsiniz.
"""
toplam = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        toplam += i

print(toplam)