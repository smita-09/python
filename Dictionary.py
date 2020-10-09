# Dictionaries : Key-Value pairs, Mutable
dict1 = {"name": "Smita",
         "Age": 23,
         "Place": "Dresden"}
print(dict1)
dict2 = dict(eye = "black")
print(dict2)
dict1["email"] = "random"
print(dict1)
# del dict1["name"], dict.pop("age"), dic.popitem() removes last inserted pair

if "name" in dict1:
    print(dict1["name"])
for key, value in dict1.items():
    print(key, value)
dict1.update(dict2)
print(dict1)
tup = ("1", "2")
dict1[tup] = 3 # cant happen with a list
print(dict1)
