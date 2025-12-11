# multiple inheritance in Python


class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"Dancer Name: {self.dance}")


class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        self.dance = dance
        self.name = name


o = DancerEmployee("Ravi", "Kathak")
# print(o.show())
print(o.name)
print(o.dance)
o.show()

print(DancerEmployee.mro())
