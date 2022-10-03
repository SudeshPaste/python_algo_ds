# Python Tuple

""" Tuple creation: """

tuple1 = (10,20,30,'Sudesh','Paste')
print(type(tuple1))

# Single value tuple
# Must be end with comma 
tuple2 = 10,
print(type(tuple2))

# creation of empt tuple
tuple3 = ()
print(type(tuple3))

# creation of tuple from list
tuple4 = tuple(['a','b','c','d'])
print(tuple4)
print(type(tuple4))

""" Accessing element of tuple """

# 1 - by using index

tuple5 = ('S','A','L','L','P')
print(tuple5[3])

# 2 - by using slice operator
tuple6 =(1,2,3,4,5,6,7,8,9,10)
print(tuple6[3:8])

""" Important function of tuple """

# len() - to find lenght of tuple
tuple7 = (1,2,3,4,5)
print(len(tuple7))

# count() - to find occurance of specific element
tuple8 = 1,2,2,2,2,3,3,4,5,5,6
print(tuple8.count(3))

# index() - find the index of specific value
tuple9 = (1,2,2,2,2,3,3,4)
print(tuple9.index(2))

# sorted() - sort the list asending order and return a list
tuple10 = (8,3,5,9,1,7,4,2)
print(sorted(tuple10))

# min() and max() - to find min and max value
tuple11 = (10,20)
print(max(tuple11))
print(min(tuple11))

""" Tuple Packing and Unpacking: """

# Packing

a=10
b=20
c=30
d=40
tuple12 = a,b,c,d
print(tuple12)

l,m,n,o = tuple12
print(l)
print(m)
print(n)
print(o)


