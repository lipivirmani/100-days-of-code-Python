# from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bidders={}
finished=False 
def find_highest_bidder(bidding_record):
  highest_bid=0
  for h in bidding_record:
    amt = bidding_record[h]
    if amt>highest_bid:
      highest_bid=amt
      winner=h
  print(f"The winner is {winner} with a bid of ${highest_bid}")
while not finished:
  name=input("What is your name? ")
  bid=int(input("What is your bid? $"))
  bidders[name]=bid
  other_bidders=input("Are there any other bidders? type 'yes ' or 'no' ")
  if other_bidders=="no":
    find_highest_bidder(bidders)
    finished=True
  elif other_bidders=="yes":
    clear()
