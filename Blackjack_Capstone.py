logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("Do you wanna play a game of blackjack? Type y or n?")
user_cards = []
computer_cards = []
is_game_over = False


def deal_card():
    card = random.choice(cards)
    return card


for _ in range(2):
     user_cards.append(deal_card())
     computer_cards.append(deal_card())

def compare(user_score,computer_score ):
    if user_score==computer_score:
        print("DRAW")
    elif computer_score==0:
        print("Lose,Opponent has BlackJack")
    elif user_score==0:
        print("Win with a BlackJack")
    elif user_score>21:
        print("You went over, you LOSE")
    elif user_score>computer_score:
        print("YOU WON HAHAHAHAH")
    elif computer_score>user_score:
        print("YOU LOSE!!!!")



def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

while  not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards {user_cards},current score:{user_score}")
    print(f"Computer's cards {computer_cards},computer score:{computer_score}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        ask=input("Type 'y' to get another card, type 'n' to pass:")
        if ask=="y":
         user_cards.append(deal_card())
        else:
          is_game_over = True
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

compare(user_score , computer_score)

