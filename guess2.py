import random
number=random.randint(1,100)
low=1
mid=50
high=100
counter=0
while True:
   if number==mid:
    print("Win")
    break
   elif number<mid:
        high=mid-1
        attemps+=1
        mid=(low+high)/2
    else:
        low=mid+1
        mid=(low+high)/2
        attempts+=1
