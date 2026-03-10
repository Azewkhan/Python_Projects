import random 

try:
  Number  = random.randint(1,100)
  Guess = int(input("Guess a nummber between 1 to 100\n"))

#Exception handling for out of range values
  if Guess > 100 or Guess < 1 :
    raise ValueError

  while Number != Guess:
    try: # Raise Value Error inside a loop to keep the system running even in case of invalid entry
      if Number > Guess:
        print("Your number is lower than actual number")
      elif Number < Guess:
        print("Your number is higher than actual number")
      Guess = int(input("Try again  "))  # Ask your Guess again
      if Guess > 100 or Guess < 1 :
        raise ValueError
      
    except ValueError:
      print("Your Value must be an integer between 1- 100")

  print("Congratulations! You guessed it correctly")

except ValueError:
  print("Your Value must be an integer between 1- 100")
except Exception as e:
  print(f'This game met an error {e}')