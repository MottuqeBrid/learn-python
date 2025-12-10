# Lamda function in Python


def double(x):
    return x * 2

print(double(5))  # Output: 10

double_lambda = lambda x: x * 2

print(double_lambda(5))  # Output: 10
square = lambda x: x * x
print(square(5))
cube = lambda x: x * x * x
print(cube(5))

sum = lambda a, b: a + b
print(sum(5, 10))
