num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
operator=input("enter the operation +,-,/,*")
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
	print(num1*num2)
elif operator == "/":
    if(num2==0):
        print("Cant divide by zero")
    else:
      print(num1/num2)
else:
    print("Invalid operations")



    