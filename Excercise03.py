#Q1
print("Welcome to the Zander Lake protection")
size = int(input("Please enter the size of the Zander you caught: "))
if size >= 42 :
    print("You can keep the Zander!")
else :
    print("The Zander is too small, please release the fish back to the water")

#Q2
cabin = input("Please enter the class of your cabin: ")
if cabin == "LUX" :
    print("You receive: upper-deck cabin with a balcony")
elif cabin == "A" :
    print("You receive: above the car deck, equipped with a window")
elif cabin == "B" :
    print("You receive: windowless cabin above the car deck.")
elif cabin == "C" :
    print("You receive: windowless cabin below the car deck")
else :
    print("Invalid cabin class")

#Q3
print("Welcome to a Hemoglobin value checker")
sex = input("Please enter your biological sex: ")
value = int(input("Please enter your hemoglobin value: "))
if sex == "female" :
    if value >= 156 :
        print("Your hemoglobin is HIGH for an adult female")
    elif value >= 117 :
        print("Your hemoglobin is NORMAL for an adult female")
    else :
        print("Your hemoglobin is LOW for an adult female")
if sex == "male" :
    if value >= 168 :
        print("Your hemoglobin is HIGH for an adult male")
    elif value >= 134 :
        print("Your hemoglobin is NORMAL for an adult male")
    else :
        print("Your hemoglobin is LOW for an adult male")
#Q4
print("Welcome to the Leap Year Detector")
year = int(input("Please enter the year you would like to check: "))
if year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
    print("The year you entered is a Leap Year!")
else :
    print("The year you entered is NOT a leap year")
