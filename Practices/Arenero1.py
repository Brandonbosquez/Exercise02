#lugar de practica de programación
import json

from flask import Flask, Response

app = Flask(__name__)

#PROBLEM 2
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
@app.route('/airport/<code>')
def airport(code):
    try:
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
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response
@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5005)





