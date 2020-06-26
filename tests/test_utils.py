import unittest
import sys
import random

sys.path.append("/Users/lukeschissler/Documents/Github/blackjack_ML")

from utils import Card, Deck

class TestCard(unittest.TestCase):
    def setUp(self):
        suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
        vals = [str(x) for x in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
        random_suits = random.choices(suits, k=20)
        random_vals = random.choices(vals, k=20)
        self.random_cards = [Card(x, y) for x, y in zip(random_vals, random_suits)]

    def test_card_init(self):
        for card in self.random_cards:
            self.assertIsInstance(card, Card)

    def test_card_return_val(self):
        for card in self.random_cards:
            card_val = card.return_val()

            if card.val in ["King", "Jack", "Queen", "10"]:
                self.assertEqual(card_val, '10')
            elif card.val == 'Ace':
                self.assertEqual(card_val, (1,11))
            else:
                self.assertEqual(card_val, card.val)

    def test_repr(self):
        for card in self.random_cards:
            self.assertEqual(str(card), f'{card.val} of {card.suit}')

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.single = Deck(1)
        self.multi = Deck(4)

    def test_deck_init(self):
        self.assertEqual([len(self.single.deck), len(self.multi.deck)],
                         [52, 208])

        for card in self.single.deck:
            self.assertIsInstance(card, Card)

        for card in self.multi.deck:
            self.assertIsInstance(card, Card)

    def test_shuffle(self):

        self.single.shuffle()
        self.multi.shuffle()

        self.assertEqual([len(self.single.deck), len(self.multi.deck)],
                            [52, 208])

        for card in self.single.deck:
            self.assertIsInstance(card, Card)

        for card in self.multi.deck:
            self.assertIsInstance(card, Card)

    def test_deal(self):
        hand1 = self.single.deal(2)

        self.assertEqual(len(hand1), 2)
        self.assertEqual(len(self.single.deck), 50)

        hand1 += (self.single.deal(2))

        self.assertEqual(len(hand1), 4)
        self.assertEqual(len(self.single.deck), 48)

        for card in hand1:
            self.assertIsInstance(card, Card)

class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        pass