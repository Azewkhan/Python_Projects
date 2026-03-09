import random

while True:
  print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
  print(f"       Your first dice number is {random.randint(1,6)}")
  print(f"       Your second dice number is {random.randint(1,6)}")
  print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
  Roll = input("Do you want to roll the dice again ? Yes/No\n").capitalize()
  if Roll == "Yes":
    continue
  else:
    break