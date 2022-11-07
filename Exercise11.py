#EXERCISE 11 - INHERITANCE
#PROBLEM 1
print("PROBLEM 1 *-*")
class Publication():
    def __init__(self,name):
        self.name = name
class Book(Publication):
    def __init__(self,name,author):
        Publication.__init__(self,name)
        self.author =author


    def print_information(self):
        print(f"\nBOOK INFORMATION")
        print(f'NAME: {self.name} 'f'\nAUTHOR: {self.author}')

class Magazine(Publication):
    def __init__(self,name,chief_editor,page_count):
        Publication.__init__(self,name)
        self.chief_editor = chief_editor
        self.page_count = page_count

    def print_information(self):
        print(f"\nMAGAZINE INFORMATION")
        print(f'NAME: {self.name} 'f'\nCHIEF EDITOR: {self.chief_editor}'f'\nPAGE COUNT: {self.page_count}')

book1 = Book("Donald Duck","Aki Hyyppä")
magazine1 = Magazine("Compartment No.6","Rosa Liksom",192)

book1.print_information()
magazine1.print_information()

#EXERCISE 2
print(f"\nEXERCISE 2 <3")
class Car:

    def __init__(self, reg_number, max_speed, current_speed=0, traveled_distance=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.current_speed = self.max_speed
        self.traveled_distance = traveled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, time):
        self.traveled_distance += time * self.current_speed
class ElectricCar(Car):
    def __init__(self,reg_number,max_speed,battery):
        Car.__init__(self,reg_number,max_speed)
        self.battery = battery

class GasolineCar(Car):
    def __init__(self,reg_number,max_speed,tank):
        Car.__init__(self,reg_number,max_speed)
        self.tank = tank

electric = ElectricCar("ABC-15", 180, "52.5 kWh")
gasoline = GasolineCar("ACD-123", 165, "32.3 l")

electric.drive(3)
gasoline.drive(3)
print(f"\n░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██""\n██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░")
print(f"PLATE     MAX SPEED      DISTANCE TRAVELED      BATTERY/TANK CAPACITY")
print(f"{electric.reg_number}     {electric.max_speed}km/h            {electric.traveled_distance}km                    {electric.battery}")
print(f"{gasoline.reg_number}    {gasoline.max_speed}km/h            {gasoline.traveled_distance}km                    {gasoline.tank}")