import art
import random
import os
os.system('cls||clear')

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

player_cards = []
dealer_cards = [] 

def deal_card(num_card,cards):
    for i in range(num_card):
        cards.append(random.choice(deck))

def calculate_score(cards):
    score = sum(cards)
    temp_cards = cards.copy()
    if score > 21:
        for i in range(len(temp_cards)):
            if temp_cards[i] == 11:
                temp_cards[i] = 1
                if sum(temp_cards) <= 21:
                    break
        score = sum(temp_cards)
    return score
    
def check_blackjack(cards):
    if calculate_score(cards) == 21:
        return True

def check_busted(cards):
    if calculate_score(cards) > 21:
        return True

def player_turn_cards():
    print(f'    Your cards: {player_cards}, current score: {calculate_score(player_cards)}')
    print(f"    Computer's first card: {dealer_cards[0]}")

def final_print():
    print('\n')
    print(f'Your cards: {player_cards}, final score: {calculate_score(player_cards)}')
    print(f"Dealer's cards: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
    exit()

# Introduction to game
if input("Do you want to play Blackjack? Type 'y' or 'n': ") == 'y':
    print(art.logo)
else:
    exit()

# Draw the first two cards for both dealer and player and print them
deal_card(2,player_cards)
deal_card(2,dealer_cards)
player_turn_cards()

# Check blackjack in 1st round
if check_blackjack(dealer_cards):
    print("Dealer has Blackjack. You lost.")
    final_print()
if check_blackjack(player_cards):
    print("You win 🙌. You have Blackjack.")
    final_print()

while True:
    cont = input("Type 'y' to get another card, others to pass: ")
    if cont == 'y':
        deal_card(1,player_cards)
        if check_blackjack(player_cards):
            print("You win 🙌. You have Blackjack.")
            final_print()
        if check_busted(player_cards):
            print("You lose 👎. You go over 21 points.")
            final_print()
        player_turn_cards()
    # dealer's turn to play
    else:
        while True:
            if calculate_score(dealer_cards) > calculate_score(player_cards):
                print("You lose 👎.")
                final_print()
            elif calculate_score(dealer_cards) == calculate_score(player_cards) and calculate_score(dealer_cards) >= 17:
                print("It's a draw! 🤝")
                final_print()
            else:
                deal_card(1,dealer_cards)
                if check_busted(dealer_cards):
                    print("You win 🙌. Dealer goes over 21 points.")
                    final_print()
    