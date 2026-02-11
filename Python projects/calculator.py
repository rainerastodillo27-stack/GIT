#python calculator

# This is a simple calculator program that performs basic arithmetic operations based on user input.
oprator = input("Enter the operator you want to use (+, -, *, /): ")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if oprator == "+":
    result = num1 + num2
    print(round(result))
elif oprator == "-":
    result = num1 - num2
    print(round(result))
elif oprator == "*":
    result = num1 * num2
    print(round(result))
elif oprator == "/":
    result = num1 / num2
    print(round(result))
else:
    print("Invalid operator! Please enter a valid operator (+, -, *, /).")
