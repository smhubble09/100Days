import os
from art import logo
print(logo)
print("Welcome to the secret auction program.")

auction = {}
highest_bid = 0
highest_bidder = ""
more_bidders = True

while more_bidders:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    result = input("Are there any other bidders? Type 'y' or 'n'\n")
    auction[name] = bid
    if result == "y":
        os.system("cls")
    else:
        more_bidders = False
        os.system("cls")

for bidder in auction:
    if auction[bidder] > highest_bid:
        highest_bid = auction[bidder]
        highest_bidder = bidder
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")