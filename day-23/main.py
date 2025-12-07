# list operations in Python
list1 = [34, 12, 5, 67, 23, 89, 1]
print("Original list:", list1)
list1.sort()
print("Sorted list:", list1)
list1.sort(reverse=True)
print("Sorted list in descending order:", list1)
list1.reverse()
print("Reversed list:", list1)
list2 = ["apple", "orange", "banana", "grape"]
print("Count of 'banana':", list2.count("banana"))

temp1=list1
temp1[0]=100
print(temp1)
print(list1)
temp2=list1.copy()
temp2[0]=109
print(temp2)
print(list1)

list1.insert(2, 45)
print("List after insertion:", list1)
list1.extend(list2)
print("List after extending:", list1)
p=list2+list1
print("Concatenated list:", p)