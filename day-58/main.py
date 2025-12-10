# constructor in python
class Person:
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age

    def info(self):
        print(f"Name: {self.name}\nOccupation: {self.occupation}\nAge: {self.age}")


a = Person("Mottuqe", "Programmer", 20)
a.info()
b = Person("Sahoreia", "Learner", 23)
b.info()
c = Person("John", "Developer", 33)
c.info()
