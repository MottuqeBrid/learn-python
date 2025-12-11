# time module in python

import time


def usingWhile():
    i = 0
    while i < 50000:
        i = i + 1
        print(i)


def usingFor():
    for i in range(50000):
        print(i)


init = time.time()
usingWhile()
t1 = time.time() - init
init = time.time()
usingFor()
t2 = time.time() - init
print(f"Time taken by while loop is {t1} seconds")
print(f"Time taken by for loop is {t2} seconds")
