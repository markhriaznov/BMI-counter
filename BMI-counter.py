name= str(input("Your name: \n"))
weight=int(input("Your weight: \n"))
height=int(input("Your height: \n"))
bmi=weight/(height*height)*10000
print (name,", your BMI is:", "%.2f" % bmi)
if bmi<25 and bmi>18:
    print ("You are in a good shape!")
elif bmi<=18: 
    print ("You have to get more fat.")
elif bmi>=25:
    print ("You should think about your appetite.")