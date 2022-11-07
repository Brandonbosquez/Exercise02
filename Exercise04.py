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
while inch >= 0 :
    print("If you want to end the program, enter a negative number")
    inch = int(input("Please enter the amount of inches to be converted: "))
    centi = inch * 2.54
    if inch >= 0 :
        print("Your value is " + str(centi) + " centimeters")
else:
    print("Program ended, goodbye")
#3
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

#5
user = "python"
word = "rules"
print("Please remember the [USERNAME] & [PASSWORD]! You have 5 attempts")
n = 0
att = 5
while n < 5 :
    user_at = input("Please enter your username: ")
    pass_at = input("Please enter your password: ")
    if user_at != user or pass_at != word :
        n = n + 1
        print("Incorrect")
        att = 5 - int(n)
        print("Attempts left: ", att)
    elif user_at == user and pass_at == word :
        print("Welcome")
        break
if att == 0 :
    print("ACCESS DENIED")
print("Program Ended")

#6 GENERATING POINTS

n = 0
run = float(input("Amount of points to be generated: "))
ins = 0
while n != run :
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    n = n + 1

    if ( x ** 2)+ ( y  ** 2) < 1 :
        ins = ins + 1

pi = float
pi = 4 * ins / run
print("The approximate value of Pi is: ", pi)





