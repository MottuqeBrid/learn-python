# static method in Python
class Math:
    def __init__(self, num):
        self.num = num

    def addToNum(self, x):
        self.num = self.num + x

    @staticmethod
    def add(x, y):
        return x + y


a = Math(10)
print(a.num)
a.addToNum(5)
print(a.num)

print(Math.add(10, 20))
