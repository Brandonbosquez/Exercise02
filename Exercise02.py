#VARIABLES AND ITERACTIVE PROGRAMS
#PHASE 1
import math
import random

name = input("Hello, what is your name? ")
print("Hello," + name + "!")

#PHASE 2
radius = float(input("Could you give the radius of your circle? "))
area = math.pi * radius **2
print("The area of your circle is:", str(area))
print(f"The area of your circle is:{area:.1f}")

#PHASE 3
print("Welcome to a Rectangle Perimeter and Area calculator")
length=float(input ("Please enter the length of your rectangle: "))
width=float(input ("Please enter the width of your rectangle: "))
perimeter = length*2 + width*2
area = length * width
print("The perimeter of your rectangle is:", str(perimeter))
print("The area of your rectangle is:", str(area))

#PHASE 4
print("Please enter 3 integer numbers, I will calculate the sum, product, and average of these numbers")
int1 = float(input("First number: "))
int2 = float(input("Second number: "))
int3 = float(input("Third number: "))
total = int1 + int2 + int3
product = int1 * int2 * int3
average = total / 3
print("The Sum of your numbers is: ", str(total))
print("The product of your numbers is: ", str(product))
print("The average of your numbers is: ", str(average))

#PHASE 5
print("welcome to the medieval units converter to kilograms and grams")
talent = float(input("please enter the mass in Talents: "))
pound = float(input("please enter the mass in Pounds: "))
lot = float(input("please enter the mass in Lots: "))
talent_con = talent * 20
pound_con = talent_con + pound
lot_con = lot + pound_con * 32
gram = lot_con * 13.3 % 1000
kilo = lot_con * 13.3 // 1000
print((f"The mass in modern units is: {kilo:.1f} kilograms and {gram:6.2f} grams"))

#PHASE 6
print("Welcome to a 3 and 4 digit code generator")
print("3-Digits Code: ")
print (f"{random.randint(0,999):03d}")
print("4-Digits Code:")
fourdcode = str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))
print(fourdcode)