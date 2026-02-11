#Shopping cart program

foods = []
prices = []
total = 0


#---while loop of the shopping cart----
while True:
    food = input("Enter a food to buy!(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the {food}: $"))
        foods.append(food)
        prices.append(price)


print("---My cart----")

for food in foods:
    print(food, end=" ")
for price in prices:
    total += price

print()
print(f"Your total is: ${total} ")














