import random 
from art import logo

def guess_number():
  number=random.randint(1,100)
  return number
  
  """To compare the guess number with the actual number"""
def compare(guess,number):
  if guess>number:
    print("Too high")
  elif guess<number:
    print("Too low")
  else:
    print("You guessed the correct number")
    
def game():
  print(logo)
  print("Welcome to the number guessing game")
  print("I am thinking of a number between 1 to 100")
  number=guess_number()
  
  level=input("Choose a difficulty level. Type 'easy' or 'hard': ")
  if level=="easy":
    attempts=10
  elif level=="hard":
    attempts=5
  while attempts>0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess=int(input("Make a guess: "))
    compare(guess,number)
    attempts-=1
    if guess==number:
      return
    elif attempts==0:
      print("You have run out of guesses. You lose")
      print(f"The correct answer is {number}")
      return
    else:
      print("Guess again")
      
game()
