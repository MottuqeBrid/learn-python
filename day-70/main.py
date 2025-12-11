# class merthod as alternative constructor in python
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def from_string(cls, str_data):
        name, age, salary = str_data.split("-")
        return cls(name, int(age), int(salary))


e = Employee("Alice", 25, 50000)
print(e.name)
print(e.age)
print(e.salary)

str_data = "Bob-30-60000"

e2 = Employee(
    str_data.split("-")[0], int(str_data.split("-")[1]), int(str_data.split("-")[2])
)
print(e2.name)
print(e2.age)
print(e2.salary)

str_data2 = "Charlie-28-55000"
e3 = Employee.from_string(str_data2)
print(e3.name)
print(e3.age)
print(e3.salary)

e4 = Employee.from_string("Dave-32-70000")
print(e4.name)
print(e4.age)
print(e4.salary)

e5 = Employee.from_string("Eve-27-48000")
print(e5.name)
print(e5.age)
print(e5.salary)
