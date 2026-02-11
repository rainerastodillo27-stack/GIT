#validate user input exercise
#user name is no meore that 12 characters
#user must not contain spaces
#user name must not cotain digits


username = input("Enter your user name: ")




if len(username) > 12:
    print("Username must be no more than 12 characters")
elif not username.find(" ") == -1:  
    print("Username must not contain spaces")
elif not username.isalpha():
    print("Your user name must not contain numbers")    
else:
    print(f"Welcome to the system!{username}")    