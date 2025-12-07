# error hendling with try-except block

a = input("Enter a number: ")
print(f"Multiplication table of {a}:")

try:
 for i in range(1, 11):
    print(f"{a} x {i} = {int(a)*i}")
except Exception as e:
    print("Error occurred:", e)
# here we can use multiiple except blocks for different exception types

print("Done")

