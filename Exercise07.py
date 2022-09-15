#EXERCISE 07 TUPLE, SET & DICTIONARY:
#1
season = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")
month = int(input("Give me the number of a month (1-12) and I will tell you what season occurs: "))
occur = season[month-1]
print("The season occuring during month #",month, " is: ", occur)


#2

direc = set()
print("Give me names and I will tell you if I have them or not")
print("To end the program enter empty string")
name = input("Enter a name: ")
while name != "":

    if name in direc :
        print("EXISTING NAME")
    else:
        print("NEW NAME")
    direc.add(name)
    name = input("Enter a name: ")
print(direc)
