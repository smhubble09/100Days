############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.

## The cards in the list have equal probability of being drawn.
## Deck of cards:
##cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
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

def final_score(p_score, d_score):
    """Returns final score and who wins"""
    if d_score == 0:
        return "Dealer got Blackjack! You lose."
    elif p_score == 0:
        return "You got Blackjack! You win!"
    elif p_score > 21:
        return "You went over. You lose."
    elif d_score > 21:
        return "Dealer bust. You win!"
    elif p_score > d_score:
        return "You win!"
    elif p_score == d_score:
        return "It's draw."
    else:
        return "Dealer wins. You lose."

def blackjack():
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
        if player_score == 0 or dealer_score == 0 or player_score >21:
            draw_again = False
            final_score(player_score, dealer_score)
        else:
            #Do you want another card?
            if input ("Type 'y' to get another card, type 'n' to pass: ") == "y":
                player_hand.append(deal_card())
            else:
                draw_again = False
                #Dealer draws
                while dealer_score < 17:
                    dealer_hand.append(deal_card())
                    dealer_score = calculate_score(dealer_hand)
                
    #Print the final score
    print(f"\nYou're final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}\n")
    print(final_score(player_score, dealer_score))
    #Do you want to play again?
    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system("cls")
        blackjack()
    else:
        print("\nGoodbye!")

blackjack()