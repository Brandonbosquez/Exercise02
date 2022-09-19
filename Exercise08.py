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
    sql = "SELECT name, municipality FROM airport"
    sql += "WHERE code = ident"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result :
            print(f"hola")
    return
code = inpout("Enter ICAO code: ")
codex(code)




