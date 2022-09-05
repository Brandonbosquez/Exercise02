#secret code

secret_code1 = "NATO"
secret_code2 = "EU"
answer = input("What is the secret code? ")
if answer == secret_code1 or answer == secret_code2 :
    print("Correct!")
else:
    print("Not correct :(")

#elif

secret_code1 = "NATO"
secret_code2 = "EU"
answer = input("What is the secret code? ")
if answer == secret_code1 :
    print("Correct!")
elif answer == secret_code2 :
    print("Also correct!")
    secret_number = int(input("What is the secret number? "))
    if secret_number == 42 :
        print("You are lucky! ;)")
else:
    print("Not correct :(")