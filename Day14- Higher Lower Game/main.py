import random 
from game_data import data
from art import logo,vs
from replit import clear


def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def formatted(a_compare,b_compare):
  """To print the data"""
  print(f"Compare A: {a_compare['name']}, a {a_compare['description']}, from {a_compare['country']}")
  print(vs)
  print(f"Against B: {b_compare['name']}, a {b_compare['description']}, from {b_compare['country']}")
  # return a_compare,b_compare

def compare_follower(a_compare,b_compare,user_input):
  a_follower=a_compare['follower_count']
  b_follower=b_compare['follower_count']
  if a_follower>b_follower:
    return user_input=='a'
  else:
    return user_input=='b'


def check(winner,user_input):
  
  if user_input==winner:
    clear()
    print("You are right")
    score=+1
    print(f"Your current score is {score}.")
    b_compare=random.choice(data)
    formatted(a_compare,b_compare)
  else:
    print("You are wrong")
    # print(f"Your final score is {score}.")
    game_over=True
    clear()
    return


def game():
  print(logo)
  score=0
  game_over=False
  a_compare = get_random_account()
  b_compare = get_random_account()
  if a_compare==b_compare:
    b_compare=get_random_account()
  
  while not game_over:
    
    a_compare=b_compare
    b_compare = get_random_account()
    formatted(a_compare,b_compare)
    user_input=input("Who has more followers? Type 'A' or 'B': ").lower()
    winner=compare_follower(a_compare,b_compare,user_input)
    clear()
    print(logo)
    if winner:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_over= True
      print(f"Sorry, that's wrong. Final score: {score}")
      
game()
