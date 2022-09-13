#1 ROLLING DICE FUNCTION
import random

def roll():
    dice = random.randint(1,6)
    while dice != 6 :
        print(dice)
        dice = random.randint(1, 6)
        print(dice)
    else:
        print("The dice roll is 6, PROGRAM ENDED")
roll()
