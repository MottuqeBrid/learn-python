# python for loop
name="Harry"
for i in name:
    print(i)
    if i=='r':
        print("This is r")

print("Done")

colors=["Red","Green","Blue","Yellow"]
for color in colors:
    print(color)
    if color=="Green":
        for i in color:
            print(i)
print("Done")

for i in range(10):
    print(i)
print("Done")
for i in range(4,10):
    print(i)
print("Done")
for i in range(1,10,2):
    print(i)

print("Done")

# reverse order
for i in range(10,0,-1):
    print(i)