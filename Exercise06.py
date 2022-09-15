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
        add += list[x]
    return add
numlist = [850, 980, 130 ]
print(adder(numlist))
print("ENDED PROBLEM 4")


#5
def even(list):
    for x in range(len(list)) :
        if x % 2 != 0 :
            list.remove(x)
    return list
numero = [1,2,3,4,5,6,7,8,9,10]
print(even(numero))

#6 EJERCICIO 6

import math
def pizza(dia, cost):
    area = ( ( dia / 2 ) ** 2 * math.pi ) / 100
    value = cost / area
    return value
print("I will tell you, between two pizzas, which one gives you the best value for your buck! ;)")
dia1 = int(input("Please enter the diameter in cm of pizza #1: "))
cost1 = int(input("Please enter the price in euros of pizza #1: "))
print("Now give me the data of pizza #2")
dia2 = int(input("Please enter the diameter in cm of pizza #2: "))
cost2 = int(input("Please enter the price in euros of pizza #2: "))
valor1= pizza(dia1,cost1)
valor2 = pizza(dia2,cost2)
if valor1 < valor2 :
    print("Pizza #1 has a lower price per square meter. BUY PIZZA #1 !!!")
else:
    print("Pizza #2 has a lower price per square meter. BUY PIZZA #2 !!!")