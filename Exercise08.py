#Ejercicio 08 RELATIONAL DATABASES
import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database ='flight_game',
    user = 'root',
    password = 'MariaDB123',
    autocommit = True
    )
def codex(code):
    sql = "select name, municipality from airport where ident = '"
    sql += code + "' ; "
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if cursor.rowcount > 0 :
        for row in response :
            print(f" Airport named: {row[0]} is located in municipality: {row[1]}")
    return

code = input("Enter ICAO code: ")
codex(code)

#Question 2

def typer(code):
    sql = " Select type, count(*) from airport where iso_country =  '"
    sql += code + "' group by type ; "
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in response:
            print(f"{row[0]} : {row[1]}")
    return

code = input("Enter the Country Code: ")
print(typer(code))

#Question 3
from geopy import distance

airportName = ["", ""]
airportPos = [[0, 0], [0, 0]]

for i in range(2):
    airportCode = input(f"Input ICAO code of airport {i + 1}: ")

    sql = "select name, latitude_deg, longitude_deg from airport "
    sql += "where ident = '" + airportCode + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airportName[i] = result[0][0]
    airportPos[i][0] = result[0][1]
    airportPos[i][1] = result[0][2]

    #print latitude and longitude of airport
    #print(airportPos[i][0])
    #print(airportPos[i][1])


print(f"Distance between {airportName[0]} and {airportName[1]} is ", end = '')
print(f"{distance.distance(airportPos[0], airportPos[1]).km:.3f} km")
#END


