# instance variables vs class variables in Python
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")


emp1 = Employee("Alice")
emp2 = Employee("Bob")

emp1.display()
emp2.display()
