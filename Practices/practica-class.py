#Practica 24.10 Class,

class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def show(self):
        print("Name is", self.name, 'ID', self.ID)

me = Student('Omelette', 2345)
me.show()

""" Create a program that:
- Will check whether the classroom is empty
- Will print the info of the classroom´s people
- If there are people, it will find out who is the highest and remove that person from the room"""

class Person:
    def __init__(self, name : str, height: int):
        self.name = name
        self.height = height
    def  __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_info(self):
        total_height = 0
        for person in self.persons:
            total_height += person.height
        print(f"There are {len(self.persons)} "
              f"persons in the room, and their combined height is "
              f"{total_height} cm")
        for person in self.persons:
            print(f'{person.name} ({person.height}) cm')

    def tallest(self):
        tallest_person = None
        height_of_tallest = 0
        for person in self.persons:
            if tallest_person is None or person.height > height_of_tallest :
                tallest_person = person
                height_of_tallest = person.height

            return tallest_person

    def remove_tallest(self):
            tallest_person = self.tallest()
            if tallest_person:
                self.persons.remove(tallest_person)

            return tallest_person

room = Room()

print("Is the room empty?", room.is_empty())
print("The tallest:", room.tallest())

room.add(Person("Giovanni", 173))
room.add(Person('Pedro', 179))
room.add(Person('Jean', 183))
room.add(Person('Maria', 154))

print()

print("Is the room empty?", room.is_empty())
print("The tallest:", room.tallest())
room.print_info()

print()

removed = room.remove_tallest()
print(f'Removed from room: {removed.name}')
room.print_info()

