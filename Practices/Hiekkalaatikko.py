#Practicas de correr


import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database ='flight_game',
    user = 'root',
    password = 'MariaDB123',
    autocommit = True
    )



code = input("Enter ICAO code: ")
SELECT airport.name, airport.municipality, FROM airport WHERE airport.ident = "00AA" ;
cursor = connection.cursor()
cursor.execute()
result = cursor.fetchall()
