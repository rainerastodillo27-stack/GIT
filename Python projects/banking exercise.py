#python bangking program

def show_balance():
    print(f"Your current balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit:"))
    
    if amount< 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    else:
        return amount
        
def withdraw():
    amount = float(input("Enter the amount to withdraw:"))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount <= 0:
        print("Amount most be greater than zero")
        return 0
    else:        
        return amount
   
    
balance = 0
is_running = True


while is_running:
    print("Welcome to the PNB banking system!")
    print("1. show the balance")
    print("2. deposit money")
    print("3. withdraw money")
    print("4. exit")


    choice = input("Enter the number (1-4 to select a options):")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()    
    elif choice == '3':
        withdraw()    
    elif choice == '4':
        is_running = False
    else:
        print("Invalid input. Please enter a number from 1-4 to select options")

print("Thank you for using the PNB banking system. Have a nice day!")