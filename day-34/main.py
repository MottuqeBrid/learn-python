# python dictionaries methods
ep1={
    "name":"John",
    "age":30,
    "city":"New York"
}
ep2={
    "country":"USA",
    "adult":True,
    "skills":["Python","JavaScript","C++"]
}


ep1.update(ep2)
# print("After update ep1 with ep2:", ep1)
# ep1.pop("age")
# print("After pop age from ep1:", ep1)
# ep1.popitem()
# print("After popitem from ep1:", ep1)
# ep1.clear()
# print("After clear ep1:", ep1)
del ep1["name"]
print("After delete name from ep1:", ep1)