# sets operations in Python

set1={2,3,4,5,6,3}
set2={5,6,7,8,9}
print("Set 1:", set1)
print("Set 2:", set2)
print(set1.union(set2))
print(set1.intersection(set2))



# print(set1,set2)
# set1.update(set2)
# print("After update Set 1:", set1) 
# set1.intersection_update(set2)
# print("After intersection update Set 1:", set1)
print(set1.symmetric_difference(set2))
print(set1.difference(set2))
print(set2.difference(set1))
