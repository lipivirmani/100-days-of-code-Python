import random
Rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images= [ Rock, Paper, Scissors]
user_ch = input("What do you want to choose ? Type 0 for Rock, 1 for Paper or 2 for Scissiors \n")
if user_ch>=0 and user_ch <=2:
    print(game_images[user_ch])

comp_ch = random.randint(0,2)
print("Computer chose : \n")
print(game_images[comp_ch])

if user_ch >= 3 or user_ch < 0:
    print("You've typed an invalid number. You lost!)
elif user_ch == 0 and comp_ch == 2:
    print("You win!")
elif comp_ch == 0 and user_ch == 2:
    print("You lose!")
elfi comp_ch > user_ch:
    print("You lose!)
elif user_ch > comp_ch:
    print("You win") 
elif comp_ch == user_ch:
    print("It's a draw!")
