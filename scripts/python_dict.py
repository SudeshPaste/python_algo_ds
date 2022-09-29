# Python Dictionary

# when we want to store values in key-value pair

"""create empty dictionary"""

dict1 = {}
print(type(dict1))

dict2 = dict()
print(type(dict2))

"""add element to dictionary"""

dict3 = {}
dict3[100] = "Sudesh"
dict3[200] = "Paste"
print(dict3)

"""Accessing dictonary element"""

dict4 = {1:"India",2:"Australia",3:"England",4:"South Africa"}
if 2 in dict4:
    print(dict4[2])   # print value of key 2

print(dict4[1])
print(dict4[4])

print(dict4.get(3))


"""Accessing dictonary element"""

dict5 = {1:"ABC",2:"LMN",3:"OPQ",4:"XYZ"}
print(dict5)
dict5[1] = "EFG"
print(dict5)


"""Delete dictonary element"""

dict6 = {"Sudesh":"Dhayari","Mahesh":"Kharadi"}
print("Before Delete ",dict6)
del dict6["Mahesh"]
print("After Delete ",dict6)
dict6.clear()
print("After Clear ",dict6)


"""Important Functions of Dictionary"""

# dict() - to create dictionary

dict7 = dict()
print(type(dict7))

# len() - to find lenght of dictionary
dict8 = {"Sudesh":"Dhayari","Mahesh":"Kharadi"}
print(len(dict8))

# clear - to clear all items dictionary
dict9 = {"Sudesh":"Dhayari","Mahesh":"Kharadi"}
dict9.clear()
print(dict9)

# get - get the value of element associated with key
dict10 = {"Sudesh":"Dhayari","Mahesh":"Kharadi"}
print(dict10.get("Sudesh"))

# pop - It removes the entry associated with the specified key and returns the corresponding value
dict11 = {100:"Sachin", 72:"Kolhi", 71:"Ponting"}
print(dict11.pop(72))
print(dict11)

# popitem - It removes an arbitrary item(key-value) from the dictionaty and returns it
dict12 = {100:"Sachin", 72:"Kolhi", 71:"Ponting"}
print(dict12.popitem())
print(dict12)

# keys() - return all keys from dictionary
dict13 = {1:2,3:4,5:6,7:8,9:10}
print(dict13.keys())

# values() - return all values from dictionary
dict14 = {1:2,3:4,5:6,7:8,9:10}
print(dict14.values())

# items() - It returns list of tuples representing key-value pairs.
dict15 = {1:2,3:4,5:6,7:8,9:10}
print(dict15.items())

# copy() - create copy of dictionary
dict16 = {"Asia":"Cricket", "Global":"Football"}
print(id(dict16))
dict17 = dict16.copy()
print(id(dict17))

# setdefault - if key present return it's value eles add record at last
dict18 = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
#print(dict18)
dict18.setdefault("SriLanka","Colombo")
print(dict18)

# update() - add dictionary to another dictionary
dict19 = {1: 'apple', 2: 'ball'}
dict20 = {'name': 'John', 'lst': [2, 4, 3]}
dict19.update(dict20)
print(dict19)

"""Dictionary Comprehension"""

dict21 = {x:x*x for x in range(10)}
print(dict21)