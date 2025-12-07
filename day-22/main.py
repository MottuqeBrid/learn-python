# list in Python
l = [1, 2, 3, 4, 5]
print(l)
print(type(l))
marks = [90, 85, 78, 92, 88]
print(marks)

# adding element to list
marks.append(95)
print(marks)
print(marks[-3])  # accessing element from the end

if 85 in marks:
    print("85 is present in marks list")
else:
    print("85 is not present in marks list")


# same things apply for strings
s = "hello world"
if "hello" in marks:
    print("hello is present in marks list")
else:
    print("hello is not present in marks list")

lst = [i*i for i in range(1, 11)]
print(lst)
lst = [i for i in range(1, 11) if i % 2 == 0]
print(lst)