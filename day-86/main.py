# Walrus Operator in python

a = True
print(a := False)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while (n := len(numbers)) > 0:
    print(numbers.pop())


foods = list()
while food := input("Enter food item: ") != "quit":
    foods.append(food)
    print(f"Adding {food} to the list.")
else:
    print("Exiting loop.")
print("Final food list:", foods)
