# super keyword in python
class ParentClass:
    def parent_method(self):
        print("ParentClass constructor")


class ChildClass(ParentClass):
    def parent_method(self):
        print("ChildClass parent_method")
        super().parent_method()

    def child_method(self):
        print("ChildClass constructor")
        super().parent_method()


p = ParentClass()
c = ChildClass()
# c.child_method()
c.parent_method()
