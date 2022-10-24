#Practica 24.10 Class,

class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def show(self):
        print("Name is", self.name, 'ID', self.ID)

me = Student('Omelette', 2345)
me.show()
