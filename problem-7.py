import time
t = time.time()
def asal_sayilar(n):
    asal = [2]
    i = 3
    while len(asal) < n:
        for a in asal:
            if i % a == 0:
                break
        else:
            asal += [i]
        i += 1
    return asal

asal_listesi = asal_sayilar(10001)
son_eleman = asal_listesi[-1]

print(son_eleman)

print(time.time()-t)