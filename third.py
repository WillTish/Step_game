counter=3
while True:
     operation=input("Enter password")
     num = "4318"
     if operation == "4318":
         print("welcome")
         break
     else:
         print("wrong password")
         counter-=1
     if counter==0:
        print("account locked")
        break 