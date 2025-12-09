# python Enumerate function

marks=[12,34,56,78,90,45, 23, 67]

# index=0
# for mark in marks:
#     print(mark)
#     if(index == 2):
#         print("index 2 is: ", mark)
#     index=index+1


for index, mark in enumerate(marks):
    print(mark)
    if(index == 2):
        print("index 2 is: ", mark)

fruits=['apple','banana','cherry']
for index, fruit in enumerate(fruits, start=2):
    print(fruit, index)
    if(index == 2):
        print("index 2 is: ", fruit)
    

