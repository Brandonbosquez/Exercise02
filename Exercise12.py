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
print(f'\nWEATHER CONDITIONS:')