import random


def password_generator():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    length = int(input("Password Length: "))



    password = ""
    for i in range(length):
        password += random.choice(characters)


    print(f"Your password is: {password}")
password_generator



