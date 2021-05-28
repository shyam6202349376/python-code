amt=int(input("enter the cash ammount:"))
print("number of 500 notes are:",amt//500)
amt=amt%500
print("number of 200 notes are:",amt//200)
amt= amt%200
print("number of 100 notes are:",amt//100)
amt= amt%100
print("number of 50 notes are:", amt//50)
amt=amt%50
print("number of 20 notes are: ", amt//20)
print("number of 10 notes are:",amt%20)

