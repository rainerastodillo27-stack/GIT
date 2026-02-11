# Membership operators = used to test whether a value or variable is found in a sequence
# (string, list, tuple, set, or dictioraies)
# in 
# not in



#------Find the letter in the secret word-----
#word = "APPLE"

#letter = input("Guess the letter in the secret word: ")
#if letter in word:
#    print(f"yOU FOUND THE SECRET {letter}")
#else:
#    print(f" Our letter is not found")    




#----List, Tuple, Set----
#students = {"Rainer", "Sobbe", "Alex"}

#student = input("inter the name of a student: ")
#if student in students:
#    print(f"{student} is a student of this school")
#else:
#    print(f"that student named {student} is not from this school")    


#----Dictionary---
#grades = {"Rainer": "A", "Alex": "B", "Sobee": "C", "Aljo": "D"}


#student = input("Enter the name of a student: ")
#if student in grades:
#    print(f"{student}'s grades is {grades[student]}")
#else:
#    print(f"{student} was not found in the database")    


#--string---

email = "rainerastodillo7@gamil.com"

if "@" in email and "." in email:
    print(f"{email} is a valid one")
else:
    print("Your {email} is incorrect or not valid")    



