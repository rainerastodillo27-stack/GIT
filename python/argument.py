#default arguments = A default value for certain parameters
# default is used when thgat argument is omitted
# make your functions more flexile, reduce # of arguments
# positional, DEFAULT, keyword, arbitrary



#def net_price(list_price, discount=0, tax=0.05):
#    return list_price * (1 - discount) * (1 + tax)

#print(net_price(500,))



#import time

#def count(start, end):
#    for x in range(start, end+1):
#        print(x)
#        time.sleep(1)
#    print("Done!")
#count(0, 10)        




#------keyword argument = an argument preceded by an indetifier helps with readability

#def hello(greeting, title, first, last):
#    print(f"{greeting} {title}{first} {last}")

#hello(greeting="hello", title="Mr.", first="Sobe", last="Membela")    

#---1-10 for loop-----
#for num in range (1, 11)
#print(x, end=" ")


#--------arbitrary--------
#*  args    = allows you to pass multiple non-key arguments
#** kwargs = allows you to pass multiple keyword-aguments
#*  unpacking opertor

#---example 1---
#def add(*args):
#    total = 0
#    for arg in args:
#        total += arg
#    return total    

#print(add(1, 2, 3))


#---example 2---
#def display_name(*args):
#    for arg in args:
#        print(arg, end=" ")

#display_name("rainer", "astodillo")



#---**kwargs----

def print_address(**houses):
    for key, value in houses.items():
        print(f"{key}: {value}")
  
print_address(street="zone 3", 
             city="EBMAGALONA", 
             state="CHOCOBALLS", 
             zip="8060")
