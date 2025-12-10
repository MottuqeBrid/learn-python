# class and object in python
class Person:
    name = "John"
    occupation = "Software Engineer"
    networth = 10

    def info(self):
        print(
            f"Name: {self.name}\nOccupation: {self.occupation}\nNetworth: {self.networth}"
        )


a = Person()
print(a.name)
a.name = "mottuqe"
print(a.name)
a.p = "hello"
print(a.p)
a.info()

b = Person()
b.name = "mottuqe"
b.info()
