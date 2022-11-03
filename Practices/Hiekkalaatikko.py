#Practicas de experimento caja de arena

import random
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


class Race:
    def __init__(self, name, distance, race_cars):
        self.name = name
        self.distance = distance
        self.race_cars = race_cars
    def hour_passes(self):
        for i in range(10):
            acc_cha = random.randint(-10, 15)
            self.race_cars[i].accelerate(acc_cha)
            self.race_cars[i].drive(1)


    def print_status(self):
        print(f"CURRENT STATUS"
              f"\nPlate     Max Speed      Current Speed       Distance Travelled       ")

        for i in range(10):
            print(
                f"{self.race_cars[i].reg_num}      {self.race_cars[i].max_spe}                {self.race_cars[i].cur_spe}                     {self.race_cars[i].dis_tra}")


    def race_finished(self):
        for i in range(10):
            if self.race_cars[i].dis_tra > 10000:
                print("RACE FINISHED")
                status == True
                break
        return status


race_cars = []

for x in range(10):
    x += 1
    reg_num = "ABC-" + str(x)
    max_spe = random.randint(100, 200)
    c = Car4(reg_num, max_spe)
    race_cars.append(c)
    print(f"Car {x} created")
    if x == 10 :
        print("Cars are ready for the race ")
        print(f"░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██""\n██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░")


print("1, 2, 3 ..." "\nGOOO!!!")
