#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    rdm_number = randint(1,100)
    number_of_guesses = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    game_result = False

    def high_or_low(num):
        if num > rdm_number:
            return "Too high."
        elif num < rdm_number:
            return "Too low."
        else:
            return 0

    if difficulty == "easy":
        number_of_guesses = 10
    else:
        number_of_guesses = 5
   
    while number_of_guesses > 0:
        number_guess = int(input("Make a guess: "))
        guess = high_or_low(number_guess)
        number_of_guesses -= 1
        if guess == 0:
            number_of_guesses = 0
            game_result = True
        elif number_of_guesses > 0:
            print("\n" + guess + "\n")
            print("Guess again.")
            print(f"You have {number_of_guesses} attempts remaining to guess the number.\n")
        else:
           print(guess)
    
    if game_result == True:
        print(f"\nYou got it! The answer was {rdm_number}")
    else:
        print(f"\nYou've run out of guesses, you lose. The number was {rdm_number}")

play_game()