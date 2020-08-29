import random
num1 = random.randint(1,9)
answer = int(input("Guess a number between 1-9 : "))
if(num1==answer):
    print("Good one, You've got it right")
else:
    print("Nice try but you got it wrong")
print("The right Ans was", num1)