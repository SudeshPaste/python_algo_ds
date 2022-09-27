# Python List

"""Creation of List Objects"""

# Defining empty list
empty_list = []
print(empty_list)

# Defining list with element
lst = ['sudesh','pune']
print(lst)

# Dynamic input from user for create a list
#list1 = eval(input("Enter list element "))
# print(list1)

# create list using list() function
list2 = list(range(10))
print(list2)
list3 = list("python")
print(list3)

# create list using split function
str1 = "Python is object oriented language"
list4 = str1.split() # default separator is whitespace
print(list4)

"""Accessing of List Objects"""

# by using index
list5 = [10,20,30,40,50]
print(list5[2]) # with positive index
print(list5[-3]) # with negative index

# by slicing
list6 = [10,20,30,40,50,60,70,80,90]
print(list6[:])
print(list6[2:5])
print(list6[:2])
print(list6[5:])
print(list6[::2])
print(list6[::-3])
print(list6[-8:-4])
print(list6[-4:-8]) # output empty list 
print(list6[1:7:-2]) # output empty list
print(list6[1:9:3])
print(list6[-2:-8:-2])
print(list6[-2:-8:2])
print(list6[2:8:-2])
print(list6[2:-8])

"""Accessing of List Objects"""

list6 = [10,20,30,40,50]
list6[0] = "A"
list6[4] = "Z"
print(list6)

"""Traversing the elements of List"""

# using while loop
list7 = ['a','b','c','d','e']
i = 0
while i < len(list7):
    print(list7[i])
    i=i+1   

# using for loop
list7 = ['a','b','c','d','e']
for i in list7:
    print(i)

# display even numbers only
list8 = [1,2,3,4,5,6,7,8,9,10]
for i in list8:
    if i % 2 == 0:
        print(i)

# display element index wise
list9 = ['mumbai','pune','chennai','kolkata']
lenght = len(list9)
for i in range(lenght):
    print(list9[i] ," at +ve position " , i , "and at -ve index " , (i-lenght))


"""Important functions of List:"""

"""
1. Get information bout list
"""

# len() - total lenghth of list
list10 = [1,2,3,4,5,6,7,8,9,10]
print(len(list10))   # output = 10

# count() - number of occurance in the list
list11 = ['a','a','a','a','d','d','s']
print(list11.count('a')) # output = 4
print(list11.count('d')) # output = 2

# index() - print index of element
list12 = [1,2,3,4,5,6,7,8,9,10]
print(list12.index(10)) # output = 9


"""
2. Manipulating elements of List
"""

# append() - append the element at last position in the list
list13 = [1,2,3,4,5]
print(list13)
list13.append("sudesh")
print(list13)

list13 = []
for i in range(101):
    if i % 10 == 0:
        list13.append(i)
print(list13)

