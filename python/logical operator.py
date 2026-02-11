#logical operator = evaluates multiple conditions (or, and, not)
#or = at least one condition is true
#and = all conditions must be true
#not = reverses the result, returns false if the result is true

#-- Example 1 - Logical operator (or)-
#temp = -5
#is_raining = True

#if temp > 35 or temp < 0 or is_raining:
#    print("The outdoor event is canccelled!")
#else:
#    print("The outdoor event is on!")    



#-- Example 2 - Logical operator (and)-
#temp = 25
#is_sunny = True

#if temp >= 28 and is_sunny:
#    print("It is hot outside Today!")
#    print("It is sunny outside today!")
#elif temp <= 0 and is_sunny:
#    print("It is cold outside today!")
#    print("It is sunny outside today!")
#elif 28 > temp > 0 and is_sunny:
#    print("It is warm outside Today!")
#    print("It is sunny outside today!")


temp = 25
is_sunny = False

if temp >= 28 and not is_sunny:
    print("It is hot outside Today!")
    print("It is cloudy outside today!")
elif temp <= 0 and is_sunny:
   print("It is cold outside today!")
   print("It is cloudy outside today!")
elif 28 > temp > 0 and is_sunny:
   print("It is warm outside Today!")
   print("It is cloudy outside today!")