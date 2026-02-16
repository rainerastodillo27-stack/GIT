#Match-case statement (Switch-case statement): An alterbative to using many 'elif' statements. It is used to match a variable against a series of values and execute a block of code based on the first match.
#Execute some code if a value matches a 'case'
#Benefits: Cleaner and syntax is more readable

def day_of_Week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Invalid day"
    
print(day_of_Week(1))    