import random
number = random.randint(1, 100)
operator=input("Enter name: ")
counter=0
while True:
    operation=int(input("Enter number: "))
    if number==operation:
        print("good job " + operator)
        print("you took " + str(counter)+ " tries")
        break
    elif operation>number:
        print("Too High")
        counter+=1
    elif operation<number:
        print("Too Low")
        counter+=1