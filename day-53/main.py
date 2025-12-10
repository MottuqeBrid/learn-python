# Map, Filter, and Reduce in Python


def cube(x):
    return x * x * x


l = [1, 2, 3, 4, 5]

# map function
new_l = list(map(lambda x: x * x * x, l))
print(new_l)
print(l)

# filter function
new_filter = filter(lambda x: x % 2 == 0, l)
print(list(new_filter))

# reduce function
