#lugar de practica de programación

#Ejercicio 08 RELATIONAL DATABASES
import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database = 'flight_game',
    user = 'root',
    password = 'MariaDB123',
    autocommit = True
    )

def co2_converter(distance):
    co2_em = distance * 112
    return co2_em
#Emissions 112g CO2/KM
#selects distance once converted from the other function for distance calculation

#3 types of packages: Gold-300pts, Silver-200pts, Bronze-100pts
#Package_type(Column to be added to airport table, containing either GOLD, SILVER, BRONZE) packet found in current location
#SCORE: Column to be added to game table to store the score of the players (Also find a way to store the ID of the player currently playing)
def points():

    sql = "select package_type from airport where ident in(select location from game);"

    cursor = connection.cursor()
    cursor.execute(sql)
    pkt = cursor.fetchall()

    if pkt == "GOLD" :
        sql = "UPDATE game SET score = score + 300 WHERE id = x ;"
        cursor = connection.cursor()
        cursor.execute(sql)

    elif pkt == "SILVER" :
        sql = "UPDATE game SET score = score + 200 WHERE id = x ;"
        cursor = connection.cursor()
        cursor.execute(sql)

    elif pkt == "BRONZE" :
        sql = "UPDATE game SET score = score + 100 WHERE id = x ;"
        cursor = connection.cursor()
        cursor.execute(sql)

    else:
        break

#Función para añadir usuario a la tabla
#Addind user
def add_user(user_name)
    sql = "INSERT INTO game VALUES ('"
    sql += user_name + "') ;"

    cursor = connection.cursor()
    cursor.execute(sql)

#Difficulty level chooser
#user chooses between Level 1 (normal), 2 (Hard), 3 (Really Hard). CO2 Budget is changed accordingly
def difficulty_level(level)






