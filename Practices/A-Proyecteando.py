#Espacio para idear el código y funciones para el proyecto de Python #

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database = 'flight_game',
    user = 'root',
    password = 'MariaDB123',
    autocommit = True
    )

from geopy import distance

def distancer(code1,code2):

    airportCodes = [code1,code2]
    airportName = ["", ""]
    airportPos = [[0, 0], [0, 0]]

    n = 0

    for i in airportCodes:

        sql = "select name, latitude_deg, longitude_deg from airport "
        sql += "where ident = '" + i + "'"

        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

       airportName[n] = result


        # print latitude and longitude of airport
        # print(airportPos[i][0])
        # print(airportPos[i][1])

    print(f"Distance between {airportName[0]} and {airportName[1]} is ", end='')
    print(f"{distance.distance(airportPos[0], airportPos[1]).km:.3f} km")

code1 = input("Enter ICAO code 1: ")
code2 = input("Enter ICAO code 2: ")
distancer(code1,code2)
    # END

