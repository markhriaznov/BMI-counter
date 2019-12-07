name= str(input("Your name:"))
weight=int(input("Your weight:"))
height=int(input("Your height:"))
bmi=weight/(height*height)*10000
print (name, ", your BMI is:", "%.2f" % bmi)
if bmi<25:
    print ("You are in a good shape!")
else: 
    print ("You need to get in a better shape :(.")
