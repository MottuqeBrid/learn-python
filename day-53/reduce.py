# Learn reduce in python

from functools import reduce

numbers = [4, 5, 1, 5, 6]

sum = reduce(lambda x, y: x + y, numbers)
print(sum)
