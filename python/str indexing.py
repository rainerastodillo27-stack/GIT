#indexing = acceessing elements of a sequence using [](indexing operator)
#[start : end : step]


credit_number = "1234-5678-9012-3456"
#start index
#print(credit_number[0])
#print(credit_number[:4])

#end index
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-1])

#step index
#print(credit_number[::2])


#exercise last digits of credit card
#last_digits = credit_number[-4:]
#print(f"****-****-****-{last_digits}")

#reverse a string
credit_number = credit_number[::-1]
print(credit_number)