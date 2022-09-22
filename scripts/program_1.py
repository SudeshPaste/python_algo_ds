import pandas as pd

lst = [1,2,3,4,5,6,7,8,9,10]
lst1 = ['A','B','C','D','E','F','G','H','I','J']

print("Accessing element using positive indexing",lst[3])

print("Accessing element using negative indexing",lst[-5]) 

print("Slicing positive step",lst[::5]) 

print("Slicing negative step",lst[::-3]) 

print("Slicing",lst[2:5]) 

print("Slicing",lst[-2:-5])   # Return empty list

print("Slicing",lst[-5:-2])

print("Slicing",lst[-5:-2])

df = pd.DataFrame(lst,columns=["number"])
print(df)

df1 = pd.DataFrame(list(zip(lst,lst1)),columns=['number','alpha'])
print(df1)

lst2 = [['Sudesh',25], ['Paste', 30],
       ['Mahesh', 26], ['Choudhari', 22]]    
df2 = pd.DataFrame(lst2, columns =['Name', 'Marks'])
print(df2)

