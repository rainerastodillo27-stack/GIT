#format specifiers = {value:flags} format a value based on what flags are inserted


price1 = 3.134567 
price2 =- 400242.56789
price3 = 12.34

# .(number)f = round to that many decimal places(fixed point number)
#print(f"price 1 is ${price1:.1f}")
#print(f"price 2 is ${price2:.1f}")
#print(f"price 3 is ${price3:.1f}")

# :(number) = allocate that many spaces for the value
#print(f"price 1 is ${price1:10}")
#print(f"price 2 is ${price2:10}")
#print(f"price 3 is ${price3:10}")

# :< = left justify
#print(f"price 1 is ${price1:<10}")
#print(f"price 2 is ${price2:<10}")
#print(f"price 3 is ${price3:<10}")

# :> = right justify
#print(f"price 1 is ${price1:>10}")
#print(f"price 2 is ${price2:>10}")
#print(f"price 3 is ${price3:>10}")

# :^ = center align
#print(f"price 1 is ${price1:^10}")
#print(f"price 2 is ${price2:^10}")
#print(f"price 3 is ${price3:^10}")

# :+ = use a plus sign to indicate positive values
#print(f"price 1 is ${price1:+10}")
#print(f"price 2 is ${price2:+10}")
#print(f"price 3 is ${price3:+10}")

# : = insert a space before positive numbers
#print(f"price 1 is ${price1: }")
#print(f"price 2 is ${price2: }")
#print(f"price 3 is ${price3: }")

# :, = use a comma as a thousands separator
print(f"price 1 is ${price1:,}")
print(f"price 2 is ${price2:,}")
print(f"price 3 is ${price3:,}")    