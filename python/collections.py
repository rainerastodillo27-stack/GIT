#collections = single "variables" used to store multiple values


# List = [] ordered and changeable, Duplicate OK

#fruits = ["banana", "orange", "apple", "grapes"]
#print(dir(fruits))
#print("apple"in fruits)
#print(len(fruits))
#print(fruits[:3])
#for fruit in fruits:
#    print(fruit)

#---re assign---
#fruits[0] = "pineapple"
#for fruit in fruits:
#    print(fruit)

#---append on a list----
#fruits.append("chocoballs")
#print(fruits)

#---remove item from list----
#fruits.remove("apple")
#print(fruits)

#---insert a item in the list----
#fruits.insert(0, "pineapple")
#print(fruits)

#----to sort and make them alpha----
#fruits.sort()
#print(fruits)

#----to reverse the items in the list----
#fruits.reverse()
#print(fruits)

#---to clear at the item in the list----
#fruits.clear()
#print(fruits)

#--to return the item on it idex----
#print(fruits.index("apple"))
#print(fruits)

#---to count and item in the list----
#print(fruits.count("banana"))
#print(fruits)



# Set = {} unoordered and immutalbe, but Add/Remove OK, No duplicates

fruits = {"banana", "orange", "apple", "grapes"}
#print(len(fruits))
#for fruit in fruits:
#fruits.add("Pineaaple")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()
print(fruits)


# Tuple = () ordered and unchangeable. Duplicate OK. Faster

fruits = {"banana", "orange", "apple", "grapes"}
#print(len(fruits)
#for fruit in fruits:
#print(fruits.count("banana"))
#print(fruits.index("apple"))

#--for loop----
for fruit in fruits:
    print(fruit)


