import random

password_length = int(input("How long would you like your password to be? "))
password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890"
#Random choices can repeat characteres , Random sample doesn't
password = random.choices(password_characters, k=password_length)
print("".join(password))