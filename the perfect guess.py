
import random
guesses= 0
n= random.randint(1,101)
a=-1
while (a !=n):
    guesses +=1
    a= int(input("enter a number between 1-100: \n"))
    if(a>n):
        print("lower number please")
    elif(a<n):
        print("higher number please")
    
print(f"you have guessed the correct number {n} in {guesses} attempts")