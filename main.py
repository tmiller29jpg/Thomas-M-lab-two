import random


game_number = random.randint(1,10)
#print(game_number)
while True:
    guess=  int(input("enter a number between 1 and 10"))

    if guess > game_number: 
        print("lower")

    elif guess < game_number:
        print ("to low")

    else:
        print("you win")
        break