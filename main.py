import random
import os

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
cards_value = {"A": 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10}


def get_card(cards):
    temp_card = cards[0]
    cards.pop(0)
    return temp_card


def game():
    cards = ["A", "A", "A", "A", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
             8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
    random.shuffle(cards)

    cards_player = []
    cards_dealer = []
    total_player = 0
    total_dealer = 0

    for i in range(2):
        cards_dealer.append(get_card(cards))
        cards_player.append(get_card(cards))

    for card in cards_dealer:
        total_dealer += cards_value[card]

    for card in cards_player:
        total_player += cards_value[card]

    os.system("cls")
    print(logo)
    print("The first dealer card is: ", end="")
    print(cards_dealer[0])
    print("Your cards are: ", end="")
    print(cards_player, end=" = ")
    print(total_player)

    while input("Type 'y' if you want to hit or 'n' if you want to stand: ") == 'y':
        temp_card = get_card(cards)
        cards_player.append(temp_card)
        total_player += cards_value[temp_card]

        if total_player > 21 and "A" in cards_player:
            total_player -= 10
            cards_player[cards_player.index("A")] = "a"

        if total_player > 21:
            os.system('cls')
            print(logo)
            print("The dealer cards are: ", end="")
            print(cards_dealer, end=" = ")
            print(total_dealer)
            print("Your cards are: ", end="")
            print(cards_player, end=" = ")
            print(total_player)
            print("Game Over!")
            print("You exceed 21 points!")
            break

        os.system('cls')
        print(logo)
        print("The first dealer card is: ", end="")
        print(cards_dealer[0])
        print("Your cards are: ", end="")
        print(cards_player, end=" = ")
        print(total_player)

    while total_dealer < 17 and total_player <= 21:
        temp_card = get_card(cards)
        cards_dealer.append(temp_card)
        total_dealer += cards_value[temp_card]

        if total_dealer > 21 and "A" in cards_dealer:
            total_dealer -= 10
            cards_dealer[cards_dealer.index("A")] = "a"

        if total_dealer > 21:
            os.system('cls')
            print(logo)
            print("The dealer cards are: ", end="")
            print(cards_dealer, end=" = ")
            print(total_dealer)
            print("Your cards are: ", end="")
            print(cards_player, end=" = ")
            print(total_player)
            print("You won!!!")
            print("Dealer exceed 21 points!")
            break

    if total_dealer <= 21 and total_player <= 21:
        os.system('cls')
        print(logo)
        print("The dealer cards are: ", end="")
        print(cards_dealer, end=" = ")
        print(total_dealer)
        print("Your cards are: ", end="")
        print(cards_player, end=" = ")
        print(total_player)

        if total_dealer < total_player:
            print("You won!!!")
        elif total_dealer > total_player:
            print("You lose!")
        else:
            print("Draw!")


print(logo)
while input("Type 1 to start a new game: ") != 0:
    os.system('cls')
    game()


