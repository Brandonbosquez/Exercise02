#EXERCISE 13
#PROBLEM 1
import json

from flask import Flask, Response

app = Flask(__name__)
@app.route('/primer/<number>')
def primer(number):
    try:
        number = float(number)
        answer = "no sé"
        if number > 1:
            for i in range(2, number // 2):
                if (number % i) == 0:
                    answer = "false"
                    return answer
            else:
                answer = "true"
                return answer
        else:
            answer = "false"
            return answer
        response = {
            "Number": number,
            "isPrime": answer,
        }
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
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

#http://127.0.0.1:5000/primer/00