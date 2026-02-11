#condtional expression = A one line if else statement(ternary operator)
#print or assign one of the two values based on a condition
# X if condition else Y


num = 5
A = 6
B = 7
age = 21
temp = 30
use_role = "admin"

#print("Positive" if num > 0 else "Negative")
#esult = "EVEN" if num % 2 == 0 else "ODD"
#min_num =A if A < B else B
#status = "Adult" if age >= 18 else "Minor"
#weather = "HOT" if temp > 20 else "COLD"
access_level = "Full Access" if use_role == "admin" else "Limited Access"

print(access_level)