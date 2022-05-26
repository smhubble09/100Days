############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from random import randint
import random
import os
from blackjack_art import logo

def calculate_score(card_list):
    """Calculates total card value in hand"""
    if len(card_list) == 2 and sum(card_list) == 21:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def deal_card():
    """Returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def final_score(p_score, p_hand, d_score, d_hand):
    """Prints final score and who wins"""
    print(f"\nYou're final hand: {p_hand}, final score: {p_score}")
    print(f"Dealer's final hand: {d_hand}, final score: {d_score}\n")
    if p_score > 21:
        print("You went over. You lose.")
    elif d_score > 21:
        print("Dealer bust. You win!")
    elif p_score > d_score:
        print("You win!")
    elif p_score == d_score:
        print("It's draw.")
    else:
        print("Dealer wins. You lose.")

def blackjack():
    # Deck of cards:
    #cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(logo)

    #Generate random cards for Dealer & Player
    dealer_hand = []
    player_hand = []
    for _ in range(2):
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())

    player_score = 0
    dealer_score = 0
    draw_again = True
    while draw_again:
        #Player current score
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        #Print cards and score
        print(f"\nYour cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}\n")

        #Detect if player or dealer has blackjack
        if player_score == 0:
            if dealer_score == 0:
                draw_again = False
                print(f"\nYou're final hand: {player_hand}")
                print(f"Dealer's final hand: {dealer_hand}\n")
                print("Dealer got Blackjack! You lose.")
            else:
                draw_again = False
                print(f"\nYou're final hand: {player_hand}")
                print(f"Dealer's final hand: {dealer_hand}\n")
                print("You got Blackjack! You win!")
        else:             
            #You lose if score is over 21
            if player_score > 21:
                draw_again = False
                final_score(player_score, player_hand, dealer_score, dealer_hand)
        
            #Do you want another card?
            elif input ("Type 'y' to get another card, type 'n' to pass: ") == "y":
                player_hand.append(deal_card)
            else:
                while dealer_score < 17:
                    dealer_hand.append(deal_card)
                    dealer_score = calculate_score(dealer_hand)
                draw_again = False
                #Print the final score
                final_score(player_score, player_hand, dealer_score, dealer_hand)
                
    #Do you want to play again?
    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system("cls")
        blackjack()
    else:
        print("\nGoodbye!")

blackjack()