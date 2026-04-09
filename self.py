# класс карта:
#     имя, масти и тд = имя масти и тд
#
# класс рука:
#     список, в который добавляются карты
#
#     подсчет суммы очков
#
# класс игра:
#     выдача карт
#
#     проверка очков
#
#         выбор игрока взять карту или хватит
#
#             проверка очков
#
#         начало цикла заново

import random
import time

class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        return sum(card.value for card in self.cards)

class Game:
    def __init__(self):
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        self.suits = ['♠️', '♥️', '♦️', '♣️']

        self.player_hand = Hand()
    def draw_card(self):
        name = random.choice(self.values)
        suit = random.choice(self.suits)

        if name in ['J','Q','K']:
            value = 10
        elif name == 'A':
            value = 11
        else:
            value = int(name)
        return Card(name,value,suit)
    def start(self):
        self.player_hand = Hand()

        self.player_hand.add_card(self.draw_card())
        self.player_hand.add_card(self.draw_card())

        print ("Карты:")
        for card in self.player_hand.cards:
            print(card.name + card.suit)
        print("Очки:", self.player_hand.get_value())


game = Game()
game.start()