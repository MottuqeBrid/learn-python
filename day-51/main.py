# python seek tell and other functions

# with open("day-51/myfile.txt", "r") as f:
#     print(type(f))
#     f.seek(10)  # move the cursor to the 10th byte
#     print(f.tell())  # get the current cursor position
#     data= f.read(5) # read 5 bytes from the current cursor position
#     print(data)
#     print(f.tell())  # get the current cursor position after reading


with open("day-51/myfile2.txt", "w") as f:
    f.write("Hello, world!")
    f.truncate(5)  # truncate the file to 5 bytes

with open("day-51/myfile2.txt", "r") as f:
    content = f.read()
    print(content)  # Output will be "Hello"
