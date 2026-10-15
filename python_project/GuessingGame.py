import random
secret = random.randint(1,20)
attempts = 3
while attempts > 0:
    guess=int(input("Guess number from 1 to 20: "))
    if guess==secret:
        print("Number Guessed")
        break
    elif guess>secret:
        print("Too High")
    else:
        print("Too low")
    attempts-=1
if attempts==0 and guess!=secret:
    print("Game Over .Number was : ",secret)                
    