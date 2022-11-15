#EXERCISE 12 - USING EXTRERNAL APIs
print("Problem 1 - CHUCK NORRIS")

print(f"\nThis is a random Chuck Norris joke: ")

import requests
import json
#https://api.chucknorris.io/jokes/random

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
#print(response) NOT NEEDED NOW
print(json.dumps(response["value"], indent=2))

#PROBLEM 2
print(f'\nPROBLEM 2 O,O')
municipality = input(f'\nWEATHER CONDITIONS:''\nMunicipality: ')
#ADD YOUR OWN KEY to variable named: key below TO TEST IT :D it is ilegal to upload the keys to Github :(
key = ""
request = "https://api.openweathermap.org/data/2.5/weather?q=" + municipality +"&appid="+ key + "&units=metric"
response = requests.get(request)
json_response = response.json()
print(json.dumps(json_response, indent=2))
try:
    response = requests.get(request)
    if response.status_code==200:
            json_response = response.json()
            # print(json.dumps(json_response, indent=2))
            print(json.dumps(json_response, indent=2))
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")