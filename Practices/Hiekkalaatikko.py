#Practicas de experimento caja de arena

import random
number = 14
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            answer = "false"
            break
        else:
            answer = "true"
            break
else:
    answer = "true"


print(answer)

