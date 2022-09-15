#Practicas de correr
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

