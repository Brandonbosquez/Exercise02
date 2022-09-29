#EXERCISE 05
#1
import random
from typing import List

#1
result = []
print("Roll the dices and I will sum up the results")
roll = int(input("How many times do you want me to roll the dice: "))
n = 0
sum = 0
while n < roll :
    n = n + 1
    luck = random.randint(1, 6)6
    result.append(luck)

for rolls in result :
    sum += rolls
print("The results of your rolls were: ", result)
print(sum)

 #2
print("Give me numbers, I will sort the biggest 5 in descending order")
numbers = []
entra = 0
print("To end the program, press ENTER")
while entra != "" :
    entra = input("Input your number: ")
    if entra != "" :
        numbers.append(int(entra))
entra = int
numbers.sort(reverse=True)
print("The five biggest numbers in descending order are:")
for x in range(5):
    print(numbers[x])

#3
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

#4
city = []
for x in range(5):
    name = input("Give me a city: ")
    city.append(name)
print("Your cities were:")
for x in city:
    print(x)
