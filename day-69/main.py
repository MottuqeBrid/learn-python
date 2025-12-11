# class methods in Python


class Emplioyee:
    compoany_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name} and the company is {self.compoany_name}")

    @classmethod
    def change_company_name(cls, new_name):
        cls.compoany_name = new_name


e1 = Emplioyee("Alice")
e1.show()
e1.change_company_name("InnoTech")
e1.show()
print(Emplioyee.compoany_name)

e2 = Emplioyee("Bob")
e2.show()
