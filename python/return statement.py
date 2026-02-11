#return = statement used to end a function and send a result to the caller

#---sample no.1------
#def add(x, y):
#    z = x + y
#    return z

#def subtract(x, y):
#    z = x - y
#    return z

#def multiply(x, y):
#    z = x * y
#    return z


#def divided(x, y):
#    z = x / y
#    return z

#print(add(1, 2))
#print(subtract(1, 2))
#print(multiply(1, 2))
#print(divided(1, 2))



#---sample no 2----

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("sobe", "membela")
print(full_name)