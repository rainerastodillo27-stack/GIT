#dictionary = a collection of {key:value} pairs 
#ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(capitals.get("USA"))

#---check if the value is in the key---
#if capitals.get("Russia"):
#    print("That capital exists")
#else:
#    print("That capital doesn't exist")    


#--use update to inset or replace a value in the key---
#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#print(capitals)


#-remove a value in the dictionary---
#capitals.pop("China")


#-remove a latest value in the dictionary---
#capitals.popitem()
#capitals.clear()


#----loop the key in the dictionaries---
#keys = capitals.keys()
#for key in capitals.keys():
#    print(keys)


#--to print every value in the dictionary--
#values = capitals.values()
#for value in capitals.values():
#    print(value)


#---to show all key and value in the dictionary---
#items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")