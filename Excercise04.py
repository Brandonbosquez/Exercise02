#1
import random

n = 1
while n <= 1000 :
    if n % 3 == 0 :
        print(str(n))
    n += 1

#2
print("Welcome to the Inches to Centimeters converter")
inch = 1
<<<<<<< HEAD
print("If you want to end the program, enter a negative number")
while inch >= 0 :
=======
while inch >= 0 :
    print("If you want to end the program, enter a negative number")
>>>>>>> 2501cfd (commit)
    inch = int(input("Please enter the amount of inches to be converted: "))
    centi = inch * 2.54
    if inch >= 0 :
        print("Your value is " + str(centi) + " centimeters")
else:
    print("Program ended, goodbye")
#3
<<<<<<< HEAD
=======
print("Smallest an biggest number detector")
number = input("Please enter a number: ")
least = number
greatest = number
while number != "" :
    if number > greatest :
        greatest = number
    if number < least :
        least = number
    print("To end the program enter an empty string (Press Enter)")
    number = input("Please enter another number: ")
    if str(number) == "" :
        break
print("Your greatest number is: ", greatest)
print("Your smallest number is: ", least)
print("Program ended")

#4
print("Let's play a guessing game. I will generate a number from 1 to 10 and you have to guess it")
number = random.randint(1,10)
guess = 0
while guess != number :
    guess = int(input("Please enter your guess: "))
    if guess > number :
        print("Too High")
    elif guess < number :
        print("Too Low")
print("Correct!")
#




>>>>>>> 2501cfd (commit)
