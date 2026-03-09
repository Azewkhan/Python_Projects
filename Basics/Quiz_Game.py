score = 0 # Should be outside of function otherwise it will reset to zero everytime
def checker (guess, correct):
  global score # If this won't be global then we can't print out a value in the final statement
  attempt = 0
  guessing = True

  while guessing and attempt<3: # Gives 3 attempt to correct your answer
    if guess.capitalize() == correct.capitalize():
      print("Congratulations! That's a correct Answer")
      score += 1
      guessing = False # Breaks the whilw loop once the answer is correct 
    else :
      print("I am sorry that's not correct")
      guess = input("Try again  ") # Takes one more input for the question and then put it in the function to check  
      attempt += 1 
  if attempt == 3:
    print(f"Sorry ! None of these answers were correct. Right answer is {correct}") # After 3 attempt gives you the answer

print("Answer the Following Questions")
Guess1 = input("Who is the Fastest Animal on the planet ?  ")
checker(Guess1,"Cheetah")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
Guess2 = input("Who is called the most loyal Animal ?  ")
checker(Guess2,"Dog")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
Guess3 = input("Who is the King of the Jungle ?  ")
checker(Guess3,"Lion")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(f"Your total score is {score} out of 3")