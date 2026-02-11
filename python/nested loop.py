#nested loop = A loop within another loop (outer, inner)

#---3times-- loop of 1-9--------
#for x in range(3):
#    for y in range(1, 10):
#        print(y, end="")
#    print()    


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a sysmbol to use: ")


for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()    