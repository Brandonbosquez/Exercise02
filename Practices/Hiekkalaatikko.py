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
            #print( f"The car's speed cannot exceed the maximum speed of the car, the speed maxes out at {self.cur_spe} km/h ")
        elif acc_prueba < 0:
            self.cur_spe = 0
            #print(f"The car's speed cannot be less than 0,the car comes to a stop")
        else:
            print("Speed change cannot be made")
        return self.cur_spe

    def drive(self, time):
        self.dis_tra += (time * self.cur_spe)
        return self.dis_tra


class Race(Car4):
    def __init__(self, name, distance, race_cars):
        self.name = name
        self.distance = distance
        self.race_cars = race_cars
    def hour_passes(self):
        for i in self.race_cars:
            if i.dis_tra < self.distance:
                i.accelerate(random.randint(-10, 15))
                i.drive(1)


    def print_status(self):
        print(f"CURRENT STATUS"
              f"\nPlate     Max Speed      Current Speed       Distance Travelled       ")

        for i in self.race_cars:
            print(
                f"{i.reg_num}      {i.max_spe}                {i.cur_spe}                     {i.dis_tra}")

    def race_finished(self):
        for i in self.race_cars:
            if i.dis_tra >= self.distance :
                print("RACE FINISHED")
                print(f"FINAL STATUS"
                      f"\nPlate     Max Speed      Current Speed       Distance Travelled       ")

                for i in self.race_cars:
                    print(
                        f"{i.reg_num}      {i.max_spe}                {i.cur_spe}                     {i.dis_tra}")
                break
            else:
                break


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


race = Race("Grand Demolition Derby",8000,race_cars)
print(f"Race called: {race.name}, has been created")
print("1, 2, 3 ..." "\nGOOO!!!")
print(f"░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██""\n██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░")

"""while True :
    for i in race.race_cars:
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()
        race.race_finished()
    break"""

a = True
hours = 1
while a == True:
    for i in race.race_cars:
        a = race.distance > i.dis_tra
        race.hour_passes()
        hours += 1
        race.race_finished()
        if hours % 10 == 0:
            race.print_status()

print(f"FINALLLLLLL" "\n ░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██")

