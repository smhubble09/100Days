#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
print("Welcome to the Python Coin Flip.")
again = "y"
while again == "y":
    result = random.randint(0,1)
    if result == 0:
        print("\nHeads")
    else:
        print("\nTails")
    again = input("\nFlip again? (y/n) ").lower()
print("\nGoodbye!")