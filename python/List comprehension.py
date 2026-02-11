#List comprehension = A concise way to create lists in python
#Compact and easier to read that traditional loops
#expression for value in iterable if condition


#double = []
#for x in range (1, 11):
#    double.append(x * 2)
#print(double)    

#-----List--------
#doubles = [x * 2 for x in range(1, 11)]
#triples = [y * 3 for y in range (1, 11)]
#squares = [z * z for z in range(1, 11)]

#print(squares)


#---string----
#fruits = ["apple", "orange", "banana", "coconut"]
#fruits = [fruit.upper() for fruit in fruits]

#print(fruits)

#---conditions----
#numbers = [1, -2, 3, -4, 5, -6]
#positive_num = [num for num in numbers if num >=0]
#print(positive_num)


grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)