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
def codex(code):

    sql = "select name and municipality from airport"
    sql += " where code = ident ; "
    return sql
code = input("Enter ICAO code: ")
codex(code)