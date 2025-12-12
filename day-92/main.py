# Function cashing in Python

import functools
import time


@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * n


print(fx(10))
print("Done for 10")
print(fx(20))  # This call will be instantaneous due to caching
print("Done for 20")
print(fx(30))
print("Done for 30")
print(fx(10))
print("Done for 10")
print(fx(20))  # This call will be instantaneous due to caching
print("Done for 20")
print(fx(30))
print("Done for 30")
