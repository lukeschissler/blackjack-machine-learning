from random import shuffle

class Card:
    def __init__(self, val: str, suit: str) -> None:
        self.val = val
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.val} of {self.suit}"

    def return_val(self):
        if self.val in ["King", "Jack", "Queen", "10"]:
            return "10"
        elif self.val in "Ace":
            return (1, 11)
        else:
            return self.val

class Deck:
    def __init__(self, num=1) -> None:
        self.num = num
        self.deck_reset()

    def deck_reset(self) -> None:
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        vals = [str(x) for x in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
        self.deck = [Card(x, y) for x in vals for y in suits] * self.num

    def shuffle(self) -> None:
        shuffle(self.deck)

    def deal(self, size) -> list:
        """Implement more true to life deal"""
        return [self.deck.pop() for x in range(size)]

class Player:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.hands = []
        self.old_hands = []
        self.antes = []
        self.split = 0

    def __repr__(self) -> str:
        return f"{self.name}: Cash - {self.cash}, Hand - {self.hands}"

    def reset(self) -> None:
        self.antes = []

    def shift_stack(self) -> None:
        self.old_hands.append(self.hands[-1])
        self.hands = self.hands[:-1]
        self.split = 0