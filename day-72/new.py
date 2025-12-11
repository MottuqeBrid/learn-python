class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}")


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}, Language: {self.lang}")


emp = Employee("John", 123)
p = Programmer("Jane", 456, "Python")
p.display()
