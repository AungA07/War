# Gage, Allan, Will, Quintaveon
import random

# deck of cards
card_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
card_suit = ['♡', "♠", "◇", "♣"]
player_values = []
computer_values = []
won_cards1 = []
won_cards2 = []
table_cards = []
table_values = []

deck = []

for suit in card_suit:
    for value in card_value:
        x = f"{value}{suit}"
        deck.append(x)

random.shuffle(deck)
player_cards = deck[0:int(len(deck) / 2)]
computer_cards = deck[int(len(deck) / 2):len(deck)]
for card in player_cards:
    if card == "2♡" or card == "2♠" or card == "2◇" or card == "2♣":
        player_values.append(2)
    elif card == "3♡" or card == "3♠" or card == "3◇" or card == "3♣":
        player_values.append(3)
    elif card == "4♡" or card == "4♠" or card == "4◇" or card == "4♣":
        player_values.append(4)
    elif card == "5♡" or card == "5♠" or card == "5◇" or card == "5♣":
        player_values.append(5)
    elif card == "6♡" or card == "6♠" or card == "6◇" or card == "6♣":
        player_values.append(6)
    elif card == "7♡" or card == "7♠" or card == "7◇" or card == "7♣":
        player_values.append(7)
    elif card == "8♡" or card == "8♠" or card == "8◇" or card == "8♣":
        player_values.append(8)
    elif card == "9♡" or card == "9♠" or card == "9◇" or card == "9♣":
        player_values.append(9)
    elif card == "10♡" or card == "10♠" or card == "10◇" or card == "10♣":
        player_values.append(10)
    elif card == "J♡" or card == "J♠" or card == "J◇" or card == "J♣":
        player_values.append(11)
    elif card == "Q♡" or card == "Q♠" or card == "Q◇" or card == "Q♣":
        player_values.append(12)
    elif card == "K♡" or card == "K♠" or card == "K◇" or card == "K♣":
        player_values.append(13)
    elif card == "A♡" or card == "A♠" or card == "A◇" or card == "A♣":
        player_values.append(14)

for card in computer_cards:
    if card == "2♡" or card == "2♠" or card == "2◇" or card == "2♣":
        computer_values.append(2)
    elif card == "3♡" or card == "3♠" or card == "3◇" or card == "3♣":
        computer_values.append(3)
    elif card == "4♡" or card == "4♠" or card == "4◇" or card == "4♣":
        computer_values.append(4)
    elif card == "5♡" or card == "5♠" or card == "5◇" or card == "5♣":
        computer_values.append(5)
    elif card == "6♡" or card == "6♠" or card == "6◇" or card == "6♣":
        computer_values.append(6)
    elif card == "7♡" or card == "7♠" or card == "7◇" or card == "7♣":
        computer_values.append(7)
    elif card == "8♡" or card == "8♠" or card == "8◇" or card == "8♣":
        computer_values.append(8)
    elif card == "9♡" or card == "9♠" or card == "9◇" or card == "9♣":
        computer_values.append(9)
    elif card == "10♡" or card == "10♠" or card == "10◇" or card == "10♣":
        computer_values.append(10)
    elif card == "J♡" or card == "J♠" or card == "J◇" or card == "J♣":
        computer_values.append(11)
    elif card == "Q♡" or card == "Q♠" or card == "Q◇" or card == "Q♣":
        computer_values.append(12)
    elif card == "K♡" or card == "K♠" or card == "K◇" or card == "K♣":
        computer_values.append(13)
    elif card == "A♡" or card == "A♠" or card == "A◇" or card == "A♣":
        computer_values.append(14)

while True:
    if len(player_values) == 0:
        break
    flip = input("Press enter to flip card!: ")
    print(player_values)
    print(player_cards)
    print(computer_values)
    print(computer_cards)
    if player_values[0] > computer_values[0]:
        if len(table_cards) > 0:
            for card in table_cards:
                won_cards1.append(card)
        won_cards1.append(player_cards[0])
        del player_cards[0]
        del player_values[0]
        won_cards1.append(player_cards[0])
        del computer_cards[0]
        del computer_values[0]
    elif player_values[0] < computer_values[0]:
        if len(table_cards) > 0:
            for card in table_cards:
                won_cards2.append(card)
        won_cards2.append(player_cards[0])
        del player_cards[0]
        del player_values[0]
        won_cards2.append(player_cards[0])
        del computer_cards[0]
        del computer_values[0]
    else:
        table_cards.append(player_cards[0])
        table_cards.append(computer_cards[0])
        del player_cards[0]
        del player_values[0]
        del computer_cards[0]
        del computer_values[0]
