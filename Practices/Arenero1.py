#lugar de practica de programación
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





