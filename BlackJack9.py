import random

BlackJack = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_Card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(cards)
    return cards


def calculate_Score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_Score, computer_Score):
    if user_Score == computer_Score:
        return "Draw"
    elif computer_Score == 0:
        return "Lose, Opponent has BlackJack"
    elif user_Score == 0:
        return "Win with a BlackJack"
    elif user_Score > 21:
        return "You went over. You lose"
    elif computer_Score > 21:
        return "Opponent went over. You win"
    elif user_Score > computer_Score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(BlackJack)
    user_Cards = []
    computer_Cards = []
    is_GameOver = False
    computer_Score = -1
    user_Score = -1

    for _ in range(2):
        user_Cards.append(deal_Card())
        computer_Cards.append(deal_Card())

    while not is_GameOver:
        user_Score = calculate_Score(user_Cards)
        computer_Score = calculate_Score(computer_Cards)
        print(f"Your Cards: {user_Cards}, current score: {user_Score}")
        print(f"Computer's first cards: {computer_Cards[0]}")

        if user_Score == 0 or computer_Cards == 0 or user_Score > 21:
            is_GameOver = True
        else:
            user_ShouldDeal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_ShouldDeal == 'y':
                user_Cards.append(deal_Card())
            else:
                is_GameOver = True

    while computer_Score != 0 and computer_Score < 17:
        computer_Cards.append(deal_Card())
        computer_Score = calculate_Score(computer_Cards)

    print(f"Your final hand: {user_Cards}, final score: {user_Score}")
    print(f"Computer's final hand: {computer_Cards}, final score: {computer_Score}")
    print(compare(user_Score, computer_Score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y ':
    print("\n" * 20)
    play_game()
