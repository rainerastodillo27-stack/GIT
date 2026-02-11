#for loops = execute a block of fixed number of times
#You can iterate a range, string, sequence, etc

#---reversed-----
#for x in reversed(range(1, 11)):
#    print(x)

#print("happy new year!")

#-----normal------
#for x in range(1, 11, 2):
#    print(x)

#------number lopps----------
#credit_card = "1234-5678-9012"

#for x in credit_card:
#    print(x)

#----continue loop and jump the given value------
#for x in range(1, 21):
#    if x == 13:
#        continue
#    else:
#        print(x)


#------break loop stop at the number before the given value---------
for x in range(1, 21):
    if x == 13:
       break
    else:
        print(x)
