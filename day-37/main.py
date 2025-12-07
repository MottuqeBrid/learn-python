# error hendling with try-except and finally block


try:
    l=[1, 2, 3]
    i=int(input("Enter an index to access element in list: "))
    print(f"Element at index {i} is {l[i]}")
except Exception as e:
    print("Error occurred:", e)
finally:
    print("Done")
