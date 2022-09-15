#Practicas de correr

print("NUMBER CLASSIFIER: I will tell you if your number is Prime")
num = int(input("Please enter your number: "))
if num > 1:
    for i in range(2, num//2):
     if (num % i) == 0:
        print("The number ", num, " is not a prime number")
        break
    else:
        print("The number ", num, " is a prime number")
else:
    print("The number ", num, " is not a prime number")

