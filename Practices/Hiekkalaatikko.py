#Practicas de experimento caja de arena

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

user = "Pedrito"
puntos = 6961

from geopy import distance
def highscore_set(username,score):
    sql = "select Highscore from game where id = '1' ; "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result[0][0])
    points = int(result[0][0])
    if cursor.rowcount > 0:
        if points < score :

            sql2 = "UPDATE game SET Highscore = '"
            sql2 += str(score) + "', screen_name = '"
            sql2 += username + "' WHERE id = '1' ; "
            cursor = connection.cursor()
            cursor.execute(sql2)
highscore_set(user,puntos)
print("DONEEEE")
