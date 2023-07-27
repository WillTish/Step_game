import random
word=random.randint(1,3)
operation=int(input(" enter 1,2,3 "))
rock=1
paper=2
scissors=3
if operation == 1:
	if word == 1:
		print("tie")
	if word == 2:
		print ("Computer Wins")
	if word == 3:
		print ("User Wins")
if operation == 2:
	if word == 2:
		print("tie")
if operation == 3:
	if word == 3:
		print("tie")
if operation == 2:
	if word == 3:
		print ("Computer Wins")
if operation == 3:
	if word == 1:
		print ("Computer Wins")
if operation == 2:
	if word == 1:
		print ("User Wins")
if operation == 3:
	if word == 2:
		print ("User Wins")

	