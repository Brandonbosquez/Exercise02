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
code= input("What is your Code: ")

codex(code)
