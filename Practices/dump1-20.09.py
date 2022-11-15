
print('PROBLEM 2 ^o^')
import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database ='flight_game',
    user = 'root',
    password = 'MariaDB123',
    autocommit = True
    )
#code = "EFHK"
code = "EFHK"
sql = "select name, municipality from airport where ident = '"
sql += code + "' ; "
cursor = connection.cursor()
cursor.execute(sql)
respons = cursor.fetchall()

airportname = respons[0][0]
location = respons[0][1]

response = {
    "ICAO": code,
    "Name": airportname,
    "Location": location, }
print(response)