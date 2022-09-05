#1
n = 1
while n <= 1000 :
    if n % 3 == 0 :
        print(str(n))
    n += 1

#2
print("Welcome to the Inches to Centimeters converter")
inch = 1
print("If you want to end the program, enter a negative number")
while inch >= 0 :
    inch = int(input("Please enter the amount of inches to be converted: "))
    centi = inch * 2.54
    if inch >= 0 :
        print("Your value is " + str(centi) + " centimeters")
else:
    print("Program ended, goodbye")
#3
