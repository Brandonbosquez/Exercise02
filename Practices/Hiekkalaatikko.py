#Practicas de correr

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

