# python string
name="John"
print(name)
print('hello '+name)



# multi line string
"""
here we can write
multiple lines
string"""
str='''hello
my name is
mottuqe'''
print(str)
print(name[0])
print(name[1])
print(name[:3])
print(name.__len__())

for char in str:
     if char!=" " and char!="\n":
        print(char)