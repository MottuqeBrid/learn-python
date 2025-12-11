# dir() _dict help() in python

# x = [1, 2, 3, 4, 5]
# print(dir(x))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("John", 30)
print(p.__dict__)
print(help(Person))


