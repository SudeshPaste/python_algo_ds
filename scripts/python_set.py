# Python set

"""Creation of Set Objects"""

set1 = {10,20,20,30,40}
print(set1)
print(type(set1))

# Empty set
set2 = set()
print(set2)
print(type(set2))

"""
Important functions of set:
"""

# 1. add() - add single element to set
set3 = {'a','b','c','d'} 
set3.add(10)
print(set3)

# 2. update() - add multiple element to set
set4 = {'sudesh','paste','pune',21}
list1 = [1,2,3,4]
set4.update(list1)
print(set4)
set4.update(range(10,15))
print(set4)

# 3. copy() - copy et object
set5 = {1,2,3,4}
set6 = set5.copy()
print(set6)

# 4. pop() - remove any random element from set
set7 = {'a','b','c','d','e'}
set7.pop()
print(set7)

# 5. remove(x) - remove x from set & if value not present
#                then give KeyError
set8 = {1,2,3,4}
set8.remove(2)
print(set8)

# 6. discard(x) - remove x from set & if value not present
#                then does not give any error
set9 = {21,23,25,27,29}
set9.discard(21)
print(set9)

# 7. clear() - remove all element from set
set10 = {'a','v','r','q'}
set10.clear()
print(set10)

"""
Mathematical operations on the Set:
"""

# 1. union - return all element from two set
set11 = {1,2,3,4}
set12 = {'a','b','c','d'}
set_union1 = set11.union(set12)
print(set_union1)
set_union2 = set11 | set12
print(set_union2)

# 2. intersection - return comman elementss from two set
set13 = {1,2,3,4,5}
set14 = {5,4,6,7,8}
set_intersection1 = set13.intersection(set14)
print(set_intersection1)
set_intersection2 = set13 & set14
print(set_intersection2)

# 3. difference() - return element present in setA but not in SetB
set15 = {10,20,30,40,50}
set16 = {10,40,80}
set_difference1 = set15.difference(set16)
print(set_difference1)
set_difference2 = set15 - set16
print(set_difference2)

# 4. symmetric_difference() - return element present in setA and SetB but not in both
set17 = {1,2,3,4,5}
set18 = {5,4,6,7,8}
print(set17 ^ set18)

"""
Membership operators: (in , not in)
"""

set19 = {1,3,5,7,9}
print(1 in set19)
print(5 not in set19)

"""
Set comprehension
"""

set20 = {x for x in range(5)}
print(set20)