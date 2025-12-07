# create custom error

a = int(input("Enter any value between 1 to 10: "))
if a<1 or a>10:
    raise ValueError("Value is out of range! It should be between 1 to 10.")
else:
    print("Value is between 1 to 10.")
