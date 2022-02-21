import random 
num=random.randint(1,9)
chances=0


while chances<5:
    
    guess=int(input("enter any number between 1 to 9:"))
    break
if(guess == num):
    print("Congratulations")

if(guess>num):
    print("try once more ,this time,try a smaller number")

if(guess<num):
    print("try once more this time,try a bigger number")

if(chances==5):
    print("you lose !!!the correct number is")

chances=chances+1


