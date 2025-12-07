# Function define in python 

a=2
b=5

def gmean(a, b):
    mean = (a*b)/(a + b)
    print(mean)

gmean(a, b)
gmean(4, 7)
gmean(4, 7)
gmean(4, 7)

def greater(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")
greater(10, 5)
greater(3, 8)
greater(5, 5)

def isless(a, b):
    # use pass keyword for leaving function body empty
    pass
