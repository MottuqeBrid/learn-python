# operator overloading in Python


class Vactor:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return Vactor(self.i + x.i, self.j + x.j, self.k + x.k)


v = Vactor(2, 3, 4)
print(v)
v2 = Vactor(5, 6, 7)
print(v2)
print(v + v2)
print(type(v + v2))
