#-----Default User and pass with login inputs-----
print("=== LOGIN ===")

correct_username = "rainer"
correct_password = "090909"

#----Students Input-------
username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful!\n")
else:
    print("Wrong username or password.")
    print("Program Ended.")
    quit()


# -------- Student Inputs --------
print("=== STUDENT INFORMATION ===")
last_name = input("Last Name: ")
first_name = input("First Name: ")

print("\nEnter Midterm Grades")

# -------- Midterm grade --------
quiz = float(input("Quiz/Activity (40%): "))
project = float(input("Project (30%): "))
exam = float(input("Exam (20%): "))
participation = float(input("Class Participation (10%): "))

midterm = (quiz * 0.40) + (project * 0.30) + (exam * 0.20) + (participation * 0.10)
print("Midterm Grade:", (midterm))

# -------- Endterm grade --------
print("\nEnter Endterm Grades")

quiz2 = float(input("Quiz/Activity (40%): "))
project2 = float(input("Project (30%): "))
exam2 = float(input("Exam (20%): "))
participation2 = float(input("Class Participation (10%): "))

endterm = (quiz2 * 0.40) + (project2 * 0.30) + (exam2 * 0.20) + (participation2 * 0.10)
print("Endterm Grade:", (endterm))


# -------- Final grade  --------
final_grade = (midterm * 0.40) + (endterm * 0.60)

print("\n=== FINAL RESULT ===")
print("Student:", first_name, last_name)
print("Final Grade:", (final_grade))


 # -------- Ang Remarks --------
if final_grade >= 90:
        print("Remarks: A")
elif final_grade >= 80:
        print("Remarks: B")
elif final_grade >= 70:
        print("Remarks: C")
elif final_grade >= 60:
        print("Remarks: D")
else:
    print("Remarks: F")

    print("Invalid input! Please enter numbers only.")