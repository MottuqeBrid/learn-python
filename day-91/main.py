# Generators in python


def my_gen():
    for i in range(5000):
        yield i


g = my_gen()
# print(next(g))
# print(next(g))
# print(next(g))
for i in g:
    print(i)
