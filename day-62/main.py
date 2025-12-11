# Acces Specificers / modifiers in Python
class Employee:
    def __init__(self, name, age, salary):
        self.name = name  # Public attribute
        self._age = age  # Protected attribute
        self.__salary = salary  # Private attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")


emp = Employee("John Doe", 30, 50000)
emp.display_info()
print(emp.name)  # Accessible
print(emp._age)  # Accessible but should be treated as protected
# print(emp.__salary)  # Not accessible, will raise AttributeError
print(emp._Employee__salary)
# print(emp.__dir__())  # To see all attributes including private ones
emp._age = 31  # Modifying protected attribute
emp.display_info()
