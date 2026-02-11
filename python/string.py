#string methods

#name = input("Enter your name: ")
#phone_number = input("Enter your phone number #: ")

#result = len(name)
#result =name.find("l")
#result =name.rfind("l")
#nanme = name.capitalize()
#name = name.upper()
#name= name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result = phone_number.count("-")
#hone_number = phone_number.replace("-", " ")

#print(help(str))


username = input("Enter your username:")

if len(username) > 12:
    print("your username must not be over 12 character")
elif not username.find(" ") == -1:
    print("your username must not contain any space")
elif not username.isalpha():
    print("Your username must cont contain digit")

else:
    print(f"Welcome {username}")


