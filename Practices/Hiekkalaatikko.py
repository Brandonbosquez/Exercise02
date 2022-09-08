#Practicas de correr
import random
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
