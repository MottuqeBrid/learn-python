# python IO operations


# f = open("day-50/myfile.txt", "r")

# while True:
#     line= f.readline()
#     print(line)
#     if not line:
#         print(line , type(line))
#         break


f = open("day-50/myfile2.txt", "w")
lines = ["This is first line\n", "This is second line\n", "This is third line\n"]
f.writelines(lines)
f.close()