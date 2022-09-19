#lugar de practica de programación

print("Welcome to the Airport database")
data = {"EFHK" : "Helsinki-Vantaa Airport",
        "MPTO" : "Tocumen International airport",
        "KMIA" : "Miami International airport"}
option = int(input("What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press 3 "))
while option != 3 :
    if option == 1 :
        code = input("Enter the ICAO code of the airport: ")
        if code in data:
            print(f"The code {code} corresponds to {data[code]}")
            option = int(input(
                "What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press 3 "))
            if option == "":
                print("PROGRAM ENDED")
                break
        else:
            print("Code was not found in the database")
            option = int(input(
                "What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press 3 "))
    if option == 2 :
        print("Selected ADD")
        code = input("Add the new code: ")
        airport = input("Add the name of the airport: ")
        data[code] = airport
        print(f"The code {code} corresponds to {airport}")
        option = input(
            "What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press ENTER ")
    else:
        print("PROGRAM ENDED")
        break
print("Thank you for using the database :)")