#Practicas de correr
points = []
import random
n = 0
run = int(input("Amount of points to be generated: "))
ins = 0
while n != run :
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    points.insert(0, x)
    points.insert(1,y)
    n = n + 1
    if points[0] ** 2 + points[1] ** 2 < 1 :
        ins = ins + 1
print(points)
pi = float
pi = 4 * ins / run
print("The approximate value of Pi is: ", pi)