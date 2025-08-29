import random

def deal_card():
    cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Ace is represented as 11
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0  # Blackjack condition         
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)  # Convert Ace from 11 to 1
        score = sum(cards)
    return score

def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
# Blackjack Game
print("Welcome to Blackjack!")
print("The goal is to get as close to 21 without going over.")
print("Aces can be 1 or 11, face cards are worth 10.")  
# Initial dealing of cards
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

is_game_over = False
should_continue = True  
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
        if should_continue == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare_scores(user_score, computer_score))
print("Thanks for playing!")

# The game is now complete and ready to be played.
