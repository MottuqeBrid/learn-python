# File IO in Python

f=open("day-49/myfile.txt", "r")
print(f)

text=f.read()
print(text)
f.close()
f=open("day-49/myfile.txt", "a")

for i in range(5):
    f.write("\nThis is line "+str(i))
f.close()
print("File written successfully")

with open("day-49/myfile.txt", "r") as f:
    text=f.read()
    print(text)