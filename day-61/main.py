# class inheritance in python


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        print(f"Employee Name: {self.name}, \nID: {self.id}")


e = Employee("Alice", 101)
e.display_info()


class Programmer(Employee):
    def show_Language(self):
        print("The default programming language is Python")


p = Programmer("Bob", 102)
p.show_Language()
p.display_info()
print(isinstance(p, Programmer))  # True
print(isinstance(p, Employee))  # True
print(issubclass(Programmer, Employee))  # True
