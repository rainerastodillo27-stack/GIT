#python weight converter
#-- This program converts weight between kilograms and pounds based on user input.
weight = float(input("Enter the weight: "))
unit = input("Enter the unit of weight (kg or lb): ")

if unit == "kg":
    weight = weight * 2.205
    unit = "lb"
    print(f"your weight is:{round(weight, 1)} {unit}")    
elif unit == "lb":
    weight = weight / 2.205
    unit = "kg"
    print(f"your weight is:{round(weight, 1)} {unit}")    
else:
    print(f"Invalid unit! Please enter either 'kg' or 'lb'.")

