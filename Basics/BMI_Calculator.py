# Exception handling
try:
  Height = float(input("Enter your height in centimeters: "))
  Weight = float(input("Enter your Weight in Kg: "))
  
  Height = Height / 100
  BMI = Weight / (Height * Height)

  print("Your Body Mass Index is:", BMI)

  if 0 < BMI < 40:
    if BMI <= 16:
      print("You are severely underweight")
    elif BMI <= 18.5:
      print("You are underweight")
    elif BMI <= 25:
      print("You are Healthy")
    elif BMI <= 30:
      print("You are overweight")
    else:
      print("You are severely overweight")
  else:
    raise ValueError # If BMI is negative or more than 40 which is impossible

except ValueError:
  print("Please enter your details in correct format") # If Someone type different dtype

except ZeroDivisionError:
  print("I am sorry but your height can't be Zero") # If someone puts Zero in height

except Exception as e:
  print(f"There is an error which says: {e}") #all other exceptions