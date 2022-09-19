#Practicas de correr

#3 Problema 3 ----------------
print("Welcome to the Airport database")
data = {"EFHK" : "Helsinki-Vantaa Airport",
        "MPTO" : "Tocumen International airport",
        "KMIA" : "Miami International airport"}
option = int(input("What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press ENTER "))

while option != "":
    while option == 1 :
        print("Selected FETCH")
        code = input("Please enter the ICAO code of the airport: ")
        while option != "" :
            if code in data :
                print(f"The code {code} corresponds to {data[code]}")
                option = int(input("What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press ENTER "))
                code = input("Please enter the ICAO code of the airport: ")
                if option = "":
                    print("PROGRAM ENDED")
                    break
            else :
                print("Code was not found in the database")
                option = int(input("What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press ENTER "))
    while option == 2 :
        print("Selected ADD")
        code = input("Add the new code: ")
        airport = input("Add the name of the airport: ")
        data[code] = airport
        print (f"The code {code} corresponds to {airport}")
        option = int(input("What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press ENTER "))
        if option = "":
            print("PROGRAM ENDED")
            break
