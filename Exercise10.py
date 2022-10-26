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
    h.go_to_floor(goto)
    print("To end pres ENTER")
    goto = int(input("To what floor should the elevator go?: "))
