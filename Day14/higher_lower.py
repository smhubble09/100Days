import random
from art import logo, vs
from game_data import data
import os

def check_answer(answer, option):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong.""" 
    if answer > option:
        return True
    else:
        return False


def play_game():
    answered_correctly = True
    correct_count = 0
    a_dict = random.choice(data)
    print(logo)
    while answered_correctly:        
        print(logo)
        b_dict = random.choice(data)
        if b_dict['name'] == a_dict['name']:
            while b_dict['name'] == a_dict['name']:
                b_dict = random.choice(data)

        print(f"Compare A: {a_dict['name']}, {a_dict['description']}, from {a_dict['country']}")
        print(vs)
        print(f"Against B: {b_dict['name']}, {b_dict['description']}, from {b_dict['country']}\n")

        player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if player_choice == "A":
            answered_correctly = check_answer(a_dict["follower_count"], b_dict["follower_count"])
        else:
            answered_correctly = check_answer(b_dict["follower_count"], a_dict["follower_count"])
        
        os.system("cls")

        if answered_correctly == True:
            a_dict = b_dict
            correct_count += 1
            print(f"You're right! Current score: {correct_count}.\n")
        else:
            print(f"Incorrect. You're final score is: {correct_count}.")

    play_again = input("\nWould you like to play again? (y/n)\n")
    if play_again == "y":
        play_game()

            

play_game()
