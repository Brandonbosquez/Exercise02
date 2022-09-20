#lugar de practica de programación

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
    sql = "SELECT airport.name, municipality, FROM airport WHERE airport.ident = " + code
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result :
            print(f"hola")
    return
code = input("Enter ICAO code: ")
codex(code)