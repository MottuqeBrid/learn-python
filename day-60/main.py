# Decorators in Python
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Good Evening")

    return mfx


@greet
def hello():
    print("Hello, World!")


@greet
def add(a, b):
    print(a + b)


hello()  # Output: Hello, World!

add(5, 10)  # Output: 15
