# -*- coding: utf-8 -*-

from random import shuffle


class Card:
    suits = ['spades', 'hearts', 'diamonds', 'clabs']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10',
              'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __ge__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + ' of ' + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_cards(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input('name of player 1\n')
        name2 = input('name of player 2\n')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = '{} won this round.'
        print(w.format(winner))

    def draw(self, p1n, p1c, p2n, p2c):
        d = '{} drew {}, {} drew {}.'
        print(d.format(p1n, p1c, p2n, p2c))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return 'Draw'

    def play_game(self):
        cards = self.deck.cards
        print('Start the War')
        while len(cards) >= 2:
            m = 'q:quit, other key:play\n'
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_cards()
            p2c = self.deck.rm_cards()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        if win != 'Draw':
            print('Game End, winner is {}!'.format(win))
        else:
            print('Game End, {}!'.format(win))


def main():
    game = Game()
    game.play_game()


if __name__ == '__main__':
    main()
