#ASSOCIATION Exercise 10
print("PROBLEM 1")

class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = int(bottom)
        self.top_floor = int(top)
        self.current_floor = self.bottom_floor

    def floor_up(self):
        if self.current_floor <= self.top_floor:
            print("Elevator moves UP")
            self.current_floor += 1
        else:
            print("Elevator has reached the top floor")

    def floor_down(self):
        if self.current_floor >= self.bottom_floor:
            print("Elevator moves DOWN")
            self.current_floor += -1
        else:
            print("Elevator has reached the bottom floor")

    def go_to_floor(self,floor_goal):
        if floor_goal < self.bottom_floor:
            return print("ERROR Elevator cannot go lower than bottom floor")
        elif floor_goal > self.top_floor:
            return print("ERROR Elevator cannot go higher than top floor")
        while self.current_floor != floor_goal :
            if floor_goal > self.current_floor:
                self.floor_up()

            elif floor_goal < self.current_floor:
                self.floor_down()

        if floor_goal == self.current_floor:
            print(f"You are currently on your desired floor: {self.current_floor}")

print("Create your very own elevator")
bottom = input("What is the bottom floor of the elevator?: ")
top = input("What is the top floor of the elevator?: ")
h = Elevator(bottom,top)
print(f"Elevator created with BOTTOM FLOOR: {h.bottom_floor} and TOP FLOOR: {h.top_floor}"
      f"\n CURRENT FLOOR: {h.current_floor}")
goto = int(input("To what floor should the elevator go?: "))
while goto != "" :
    h.go_to_floor(int(goto))
    print("To end pres ENTER")
    goto = input("To what floor should the elevator go?: ")

#Problem 2
print("PROBLEMA 2 :D")

class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = int(bottom)
        self.top_floor = int(top)
        self.current_floor = self.bottom_floor

    def floor_up(self):
        if self.current_floor <= self.top_floor:
            print("Elevator moves UP")
            self.current_floor += 1
        else:
            print("Elevator has reached the top floor")

    def floor_down(self):
        if self.current_floor >= self.bottom_floor:
            print("Elevator moves DOWN")
            self.current_floor += -1
        else:
            print("Elevator has reached the bottom floor")

    def go_to_floor(self,floor_goal):
        if floor_goal < self.bottom_floor:
            return print("ERROR Elevator cannot go lower than bottom floor")
        elif floor_goal > self.top_floor:
            return print("ERROR Elevator cannot go higher than top floor")
        while self.current_floor != floor_goal :
            if floor_goal > self.current_floor:
                self.floor_up()

            elif floor_goal < self.current_floor:
                self.floor_down()

        if floor_goal == self.current_floor:
            print(f"You are currently on your desired floor: {self.current_floor}")
class Building(Elevator):
    def __init__(self, bottom, top, elevators):

        self.num_of_elevators = int(elevators)
        self.elevators= []
        for i in range(int(self.num_of_elevators)):
            i = super().__init__(bottom, top)
            self.elevators.append(i)

    def run_elevator(self, num, destin):
        elevator_num = int(num) - 1
        self.elevators[elevator_num] = super().go_to_floor(destin)

print("Let's create a building with different elevators")
bot_floor = input("What will be the bottom floor?: ")
top_floor = input("What will be the top floor?: ")
num_elevators = input("How many elevators will the building have?: ")

building1 = Building(bot_floor,top_floor,num_elevators)
elevator_number = input("What elevator do you wish to move?: ")
destination = int(input("Where should the elevator move?: "))
building1.run_elevator(elevator_number, destination)

#PROBLEM 3
print("PROBLEM 3 (^o.o^)")

class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = int(bottom)
        self.top_floor = int(top)
        self.current_floor = self.bottom_floor

    def floor_up(self):
        if self.current_floor <= self.top_floor:
            print("Elevator moves UP")
            self.current_floor += 1
        else:
            print("Elevator has reached the top floor")

    def floor_down(self):
        if self.current_floor >= self.bottom_floor:
            print("Elevator moves DOWN")
            self.current_floor += -1
        else:
            print("Elevator has reached the bottom floor")

    def go_to_floor(self,floor_goal):
        if floor_goal < self.bottom_floor:
            return print("ERROR Elevator cannot go lower than bottom floor")
        elif floor_goal > self.top_floor:
            return print("ERROR Elevator cannot go higher than top floor")
        while self.current_floor != floor_goal :
            if floor_goal > self.current_floor:
                self.floor_up()

            elif floor_goal < self.current_floor:
                self.floor_down()

        if floor_goal == self.current_floor:
            print(f"You are currently on your desired floor: {self.current_floor}")
class Building(Elevator):
    def __init__(self, bottom, top, elevators):

        self.num_of_elevators = int(elevators)
        self.elevators= []
        for i in range(int(self.num_of_elevators)):
            i = super().__init__(bottom, top)
            self.elevators.append(i)

    def run_elevator(self, num, destin):
        elevator_num = int(num) - 1
        self.elevators[elevator_num] = super().go_to_floor(destin)

    def fire_alarm(self):
        print("FIRE ALARM: All elevators sent to bottom floor")
        for i in range(len(self.elevators)):
            self.elevators[i] = super().go_to_floor(self.bottom_floor)
            print(f"Elevator #{i+1} reached BOTTOM FLOOR")

print("Let's create a building with different elevators")
bot_floor = input("What will be the bottom floor?: ")
top_floor = input("What will be the top floor?: ")
num_elevators = input("How many elevators will the building have?: ")

building1 = Building(bot_floor,top_floor,num_elevators)
elevator_number = input("What elevator do you wish to move?: ")
destination = int(input("Where should the elevator move?: "))
building1.run_elevator(elevator_number, destination)
building1.fire_alarm()

#PROBLEM 4
print('PROBLEM 4 O.O')

import random
class Car:

    def __init__(self, reg_number, max_speed, current_speed=0, traveled_distance=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, time):
        self.traveled_distance += time * self.current_speed


class Race:
    def __init__(self, race_name, distance, cars):
        self.cars = []
        self.cars.extend(cars)
        self.name = race_name
        self.distance = distance
        self.timer = 0

    def hour_passes(self):
        for car in range(len(self.cars)):
            self.cars[car].drive(1)
            self.cars[car].accelerate(random.randint(-10, 15))
            if car == 9:
                self.timer += 1
            if self.timer % 10 == 0 and car == 9:
                print(f"\n{self.timer} hours has passed")
                self.print_status()

    def print_status(self):
        print(f"\nPlate     Max Speed      Current Speed       Distance Travelled       ")
        for car in range(len(self.cars)):
            print(f"{self.cars[car].reg_number}      {self.cars[car].max_speed}km/h          {self.cars[car].current_speed}km/h                 {self.cars[car].traveled_distance}km")
    def race_finished(self):
        for car in range(len(self.cars)):
            if self.cars[car].traveled_distance >= self.distance:
                print(f"░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██""\n██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░")
                print(f"\n\nThe car {self.cars[car].reg_number} won the race!!")
                print(f"░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██""\n██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░")
                self.print_status()
                print("END OF RACE")
                return True



car_list = []
for i in range(0, 10):
    new_car = Car("ABC-" + str(i+1), random.randint(100, 200))
    car_list.append(new_car)

# main
race = Race("Grand Demolition Derby", 8000, car_list)
print(f"Welcome to the {race.name} race!")
print("Cars are ready for the race ")
print(f"░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██""\n██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░")

while not race.race_finished():
    race.hour_passes()






