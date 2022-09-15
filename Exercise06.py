#1 ROLLING DICE FUNCTION
import random

def roll():
    return random.randint(1,6)

roll()
while roll() != 6:
    print(roll())
    roll()
    print(roll())
else:
    print("The dice roll is 6, PROGRAM ENDED")

#2

print("I will give the dice as many sides as you want, and roll it until it hits the maximum value")
def roll2(x):
    return random.randint(1,x)
x = int(input("How many sides should the dice have? "))
roll2(x)
while roll2(x) != x :
    print(roll2(x))
else:
    print("The dice has reached ", x, ", PROGRAM ENDED")

#3
print("US Gallon to Liter converter. To end the program input a negative value")
def gallit(g):
    return g * 4.546
g = int(input("How many US Gallons do you want to convert to Liters?: "))
while g > 0 :
    print(g, " Gallons is: ", gallit(g), " Liters")
    g = int(input("How many US Gallons do you want to convert to Liters?: "))
else:
    print("Negative value entered. PROGRAM ENDED")

#4

def adder(list):
    add = 0
    for x in range(len(list)):
        sum += list[x]
    return sum
numlist = [850, 980, 130 ]
print(adder(numlist))


#5

