# Exercise 09
# Object oriented programming

# Problem 1

class Car:
    def __init__(self,reg_num,max_spe):
        self.reg_num = reg_num
        self.max_spe = max_spe, "km/h",
        self.cur_spe = 0
        self.dis_tra = 0

carro1 = Car("ABC-123", 142)

print(f"The car's registration number is {carro1.reg_num}, maximum speed: {carro1.max_spe}, current speed: {carro1.cur_spe}, distance traveled {carro1.dis_tra}")

#Problem 2
print("PROBLEM 2 <3")
class Car2:
    def __init__(self,reg_num,max_spe):
        self.reg_num = reg_num
        self.max_spe = max_spe
        self.cur_spe = 0
        self.dis_tra = 0

    def accelerate(self,spe_cha):
        acc_prueba = self.cur_spe + spe_cha
        if acc_prueba > 0 and acc_prueba < self.max_spe:
            self.cur_spe += spe_cha
        elif acc_prueba > self.max_spe:
            self.cur_spe = self.max_spe
            print(f"The car's speed cannot exceed the maximum speed of the car, the speed maxes out at {self.cur_spe} km/h ")
        elif acc_prueba < 0:
            self.cur_spe = 0
            print(f"The car's speed cannot be less than 0,the car comes to a stop")
        else:
            print("Speed change cannot be made")
        return self.cur_spe

carro1x = Car2("ABC-123", 142)

print(f"The car's registration number is {carro1x.reg_num}, maximum speed: {carro1x.max_spe}, current speed: {carro1x.cur_spe}, distance traveled {carro1x.dis_tra}")
#Car accelerates 30, 70, and 50 km/h

carro1x.accelerate(30)
print("Car accelerates: 30 km/h ")
print(f"Car's current speed is: {carro1x.cur_spe} km/h" )

carro1x.accelerate(70)
print("Car accelerates: 70 km/h ")
print(f"Car's current speed is: {carro1x.cur_spe} km/h" )


print("Car accelerates: 50 km/h ")
carro1x.accelerate(50)
print(f"Car's current speed is: {carro1x.cur_spe} km/h" )

print("Car emergency breaks: -200 km/h")
carro1x.accelerate(-200)
print(f"Car's current speed is: {carro1x.cur_spe} km/h" )

#Problem 3
print("PROBLEMA 3")





