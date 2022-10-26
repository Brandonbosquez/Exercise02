# Exercise 09
# Object oriented programming
import random

# Problem 1
print("PROBLEM 1 :)")


class Car:
    def __init__(self, reg_num, max_spe):
        self.reg_num = reg_num
        self.max_spe = max_spe, "km/h",
        self.cur_spe = 0
        self.dis_tra = 0


carro1 = Car("ABC-123", 142)

print(
    f"The car's registration number is {carro1.reg_num}, maximum speed: {carro1.max_spe}, current speed: {carro1.cur_spe}, distance traveled {carro1.dis_tra}")

# Problem 2
print("PROBLEM 2 <3")


class Car2:
    def __init__(self, reg_num, max_spe):
        self.reg_num = reg_num
        self.max_spe = max_spe
        self.cur_spe = 0
        self.dis_tra = 0

    def accelerate(self, spe_cha):
        acc_prueba = self.cur_spe + spe_cha
        if acc_prueba > 0 and acc_prueba < self.max_spe:
            self.cur_spe += spe_cha
        elif acc_prueba > self.max_spe:
            self.cur_spe = self.max_spe
            print(
                f"The car's speed cannot exceed the maximum speed of the car, the speed maxes out at {self.cur_spe} km/h ")
        elif acc_prueba < 0:
            self.cur_spe = 0
            print(f"The car's speed cannot be less than 0,the car comes to a stop")
        else:
            print("Speed change cannot be made")
        return self.cur_spe


carro1x = Car2("ABC-123", 142)

print(
    f"The car's registration number is {carro1x.reg_num}, maximum speed: {carro1x.max_spe}, current speed: {carro1x.cur_spe}, distance traveled {carro1x.dis_tra}")
# Car accelerates 30, 70, and 50 km/h

carro1x.accelerate(30)
print("Car accelerates: 30 km/h ")
print(f"Car's current speed is: {carro1x.cur_spe} km/h")

carro1x.accelerate(70)
print("Car accelerates: 70 km/h ")
print(f"Car's current speed is: {carro1x.cur_spe} km/h")

print("Car accelerates: 50 km/h ")
carro1x.accelerate(50)
print(f"Car's current speed is: {carro1x.cur_spe} km/h")

print("Car emergency breaks: -200 km/h")
carro1x.accelerate(-200)
print(f"Car's current speed is: {carro1x.cur_spe} km/h")

# Problem 3
print("PROBLEMA 3")


class Car3:
    def __init__(self, reg_num, max_spe):
        self.reg_num = reg_num
        self.max_spe = max_spe
        self.cur_spe = 60
        self.dis_tra = 2000

    def accelerate(self, spe_cha):
        acc_prueba = self.cur_spe + spe_cha
        if acc_prueba > 0 and acc_prueba < self.max_spe:
            self.cur_spe += spe_cha
        elif acc_prueba > self.max_spe:
            self.cur_spe = self.max_spe
            print(
                f"The car's speed cannot exceed the maximum speed of the car, the speed maxes out at {self.cur_spe} km/h ")
        elif acc_prueba < 0:
            self.cur_spe = 0
            print(f"The car's speed cannot be less than 0,the car comes to a stop")
        else:
            print("Speed change cannot be made")
        return self.cur_spe

    def drive(self, time):
        self.dis_tra += (time * self.cur_spe)
        return self.dis_tra


carro2 = Car3("ABC-321", 142)
carro2.drive(1.5)
print("Car drives for 1.5 hours")
print(f"Distance travelled by the car is {carro2.dis_tra}")

# Problem 4
print("PROBLEM 4 '_' ")


class Car4:
    def __init__(self, reg_num, max_spe):
        self.reg_num = reg_num
        self.max_spe = max_spe
        self.cur_spe = 0
        self.dis_tra = 0

    def accelerate(self, spe_cha):
        acc_prueba = self.cur_spe + spe_cha
        if acc_prueba > 0 and acc_prueba < self.max_spe:
            self.cur_spe += spe_cha
        elif acc_prueba > self.max_spe:
            self.cur_spe = self.max_spe
            print(
                f"The car's speed cannot exceed the maximum speed of the car, the speed maxes out at {self.cur_spe} km/h ")
        elif acc_prueba < 0:
            self.cur_spe = 0
            print(f"The car's speed cannot be less than 0,the car comes to a stop")
        else:
            print("Speed change cannot be made")
        return self.cur_spe

    def drive(self, time):
        self.dis_tra += (time * self.cur_spe)
        return self.dis_tra


race_cars = []

for x in range(10):
    x += 1
    reg_num = "ABC-" + str(x)
    max_spe = random.randint(100,200)
    c = Car4(reg_num,max_spe)
    race_cars.append(c)
    print(f"Car {x} created")

print("Cars ready for race")
print("1, 2, 3 ..." "\nGOOO!!!")

while True:
    for i in range(10):
        acc_cha = random.randint(-10 , 15)
        race_cars[i].accelerate(acc_cha)
        race_cars[i].drive(1)
    if race_cars[i].dis_tra > 10000:
        print("Race ended")
        break

print(f"RACE RESULTS"
      f"\nPlate     Max Speed      Current Speed       Distance Travelled       ")

for i in range(10):
    print(f"{race_cars[i].reg_num}      {race_cars[i].max_spe}                {race_cars[i].cur_spe}                     {race_cars[i].dis_tra}")

