# ----REGESTRATION----
print("=== REGISTRATION ===")
username = input("Create Username: ")
password = input("Create Password: ")
Student_name = input("Enter Student Name: ")


# ----LOGIN----
print("\n=== LOGIN ===")
user = input("Enter Username: ")
passw = input("Enter Password: ")

if user == username and passw == password:
    print("Login Successful!\n")
else:
    print("Wrong username or password")
    quit()


# ----STUDENT INFORMATION INPUT----
print("=== STUDENT INFORMATION ===")

lname = input("Last Name: ")
fname = input("First Name: ")
mname = input("Middle Name: ")
course = input("Course, Year & Section: ")


# ----Midterm Grade computation----
print("\n--- MIDTERM GRADES ---")

# Academic Records Grade is (40%)
print("Academic Records")
quiz = float(input("Quiz: "))
oral = float(input("Oral Quiz: "))
activity = float(input("Activity: "))

academic = (quiz + oral + activity) / 3
academic = academic * 0.40
print("Academic Score:", academic)


# Project Grade is (30%)
print("\nProject")
system = float(input("System: "))
documents = float(input("Documents: "))

project = (system * 0.60) + (documents * 0.40)
project = project * 0.30
print("Project Score:", project)


# Exam Grade is(20%)
print("\nExam")
exam = float(input("Exam Grade: "))
exam = exam * 0.20
print("Exam Score:", exam)


# -----Class Participation Grade is (10%)-----
print("\nClass Participation")
research = float(input("Research: "))
attendance = float(input("Attendance: "))
certificate = float(input("Certificate: "))

participation = (research + attendance + certificate) / 3
participation = participation * 0.10
print("Participation Score:", participation)


# ----Midterm Total Grade----
midterm = academic + project + exam + participation
print("\nMidterm Grade:", midterm)


# ------- ENDTERM ------
print("\n--- ENDTERM GRADES ---")

# -----Academic Records (40%)----
print("\nAcademic Records")
quiz = float(input("Quiz: "))
oral = float(input("Oral Quiz: "))
activity = float(input("Activity: "))

academic = (quiz + oral + activity) / 3
academic = academic * 0.40
print("Academic Score:", academic)


# -----Project (30%)-----
print("\nProject")
system = float(input("System: "))
documents = float(input("Documents: "))

project = (system * 0.60) + (documents * 0.40)
project = project * 0.30
print("Project Score:", project)


# -----Exam (20%)-----
print("\nExam")
exam = float(input("Exam Grade: "))
exam = exam * 0.20
print("Exam Score:", exam)


# -----Class Participation (10%)-----
print("\nClass Participation")
research = float(input("Research: "))
attendance = float(input("Attendance: "))
certificate = float(input("Certificate: "))

participation = (research + attendance + certificate) / 3
participation = participation * 0.10
print("Participation Score:", participation)


# Endterm Total
endterm = academic + project + exam + participation
print("\nEndterm Grade:", endterm)



# ----Final Grade Computation----
final = (midterm * 0.45) + (endterm * 0.55)

print("\n--- FINAL RESULT ---")
print("Student:", fname, mname, lname)
print("Course:", course)
print("Final Grade:", final)


# -----Remarks-----
if final >= 90:
    print("Remarks: A")
elif final >= 80:
    print("Remarks: B")
elif final >= 70:
    print("Remarks: C")
elif final >= 60:
    print("Remarks: D")
else:
    print("Remarks: F")

quit()