unit = input("Enter the unit of temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))
if unit == "C":
    temp = round(temp * 9/5 + 32, 1)
    unit = "F"
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 2)
    unit = "C"
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print("Invalid unit! Please enter either 'C' for Celsius or 'F' for Fahrenheit.")
