# python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount must be greater or equal than zero. Please try again.")
    else:
        break    

while True:
    rate = float(input("Enter the Interest rate: "))
    if rate < 0:
        print("Interest rate must be greater or equal than zero. Please try again.")
    else:
        break    

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("time must be greater or equal than zero. Please try again.")
    else:
        break    


total = principle * pow((1 + rate / 100), time)
print(f"Balance after our {time} year/s: ${total:.2f}")