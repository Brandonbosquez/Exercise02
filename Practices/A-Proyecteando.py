#Espacio para idear el código y funciones para el proyecto de Python #
import random

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




#FUNCIÓN RANDOMIZADORA:::

current = "Helsinki Vantaa Airport"
def five_locations(current):

    sql = "SELECT name FROM airport WHERE name <> '" + current + "' ;"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airports = []
    for x in range (116):
        airports.append(result[x][0])
    print(airports)

    return airports

def index_selection(airports):
    chosen = random.sample(airports, 5)
    i = print(chosen)
    return i



index_selection(five_locations(current))