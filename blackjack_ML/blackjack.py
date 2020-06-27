from AIs import dealer_ai, ml_ai
from utils import (
    Deck,
    Player,
    AiPlayer
)


class BlackJack:
    """Blackjack game object. Handles deck creation, dealing, playing, and turn assessment."""

    def __init__(self, players, deck_num=1, turns=1, ante=50, outs=False) -> None:
        """

        :param players: Instances of Player class
        :param deck_num: Number of decks to play with. Default: 1
        :param turns: How many turns to play. Default: 1
        :param ante: Set the ante for the game. Default:  1
        :param outs: Set whether to print notification outstrings. Default:  Don't print.
        """
        self.players = players
        self.turns = turns
        self.deck = Deck(deck_num)
        self.ante = ante
        self.outs = outs

    def optional_print(self, msg):
        if self.outs:
            print(msg)

    def deal(self) -> None:
        """Deal cards to players.  Increase deck size if too small to deal."""
        if len(self.deck.deck) < len(self.players) * 4 + 52:
            self.deck.deck_reset()
            self.deck.shuffle()

        for player in self.players:
            player.hands.append(self.deck.deal(2))

    def check_hand(self, player) -> None:
        if player.hands:
            hand_sum = self.sum_hand(player.hands[-1])
            if 21 in hand_sum or all(j > 21 for j in hand_sum):
                player.shift_stack()

    def dealer_hand(self, state) -> list:
        """Access the dealers current or played hand."""
        for player in self.players:
            if player.func == dealer_ai:
                if state == "curr":
                    return player.hands
                if state == "played":
                    return player.played_hands

    def sum_hand(self, hand) -> list:
        """Return the sum(s) of a player's hand."""
        sums = [0]

        for card in hand:
            if card.val == "Ace":
                sums = [x + 1 for x in sums] + [x + 11 for x in sums]
            else:
                sums = [x + int(card.return_val()) for x in sums]
        return sorted(set(sums))

    def turn(self, player: Player) -> None:
        """Play a turn of blackjack.  Breaks when there are no moves to make or the player stands on all hands."""
        player.cash -= self.ante
        player.antes.append(self.ante)

        while player.hands:
            move = player.func(
                hand_sum=self.sum_hand(player.hands[-1]),
                dealer_card=self.d1_card,
                player=player,
                outs=self.outs,
            )
            self.optional_print(str(player.name) + " -> " + move)
            if len(player.hands[-1]) > 2 and move == "d":
                move = "h"

            if move == "p" and len(player.hands) == 1:
                player.split = 1
                player.antes.append(self.ante)
                player.cash -= self.ante
                player.hands = [
                    [player.hands[-1][0]] + self.deck.deal(1),
                    [player.hands[-1][1]] + self.deck.deal(1),
                ]

            elif move == "d":
                player.hands[-1] += self.deck.deal(1)
                player.cash -= self.ante
                player.antes[-1] += self.ante
                player.shift_stack()

            elif move == "h":
                player.hands[-1] += self.deck.deal(1)

            else:
                player.shift_stack()

            self.check_hand()

    def play(self) -> None:
        """Take turns for all players, settle up, and reset for the next turn."""
        self.deck.shuffle()
        for i in range(self.turns):
            self.optional_print("\n" + "It's a new deal!")
            self.deal()
            self.d1_card = self.dealer_hand("curr")[0][0]

            for player in self.players:
                self.turn(player)

            self.settlement()
            self.reset()

    def compare_hands(self, dealer_score, player):
        for hand, ante in zip(player.played_hands, player.antes):
            hand_sum = self.sum_hand(hand)
            try:
                score = max([x for x in hand_sum if x < 22])
            except:
                score = []

            if not score:
                self.optional_print(f"{player.name} busted with {score} and lost {ante}")
            elif score == dealer_score:
                player.cash += ante
                self.optional_print(f"{player.name} tied dealer with {score} and made back their ante of {ante}")
            elif score < dealer_score:
                self.optional_print(f"{player.name} lost to the dealer with {score} and lost {ante}")
            elif score == 21 and len(hand) == 2:
                player.cash += ante + ante * (3 / 2)
                self.optional_print(f"{player.name} won with blackjack and made {ante +ante * (3 / 2)}")
            else:
                player.cash += ante * 2
                self.optional_print(f"{player.name} won with {score} and made {ante * 2}")

    def settlement(self):
        """Assess and distribute winnings from a hand."""
        d_hand = self.dealer_hand("played")
        dealer_score = max([x if x < 22 else 0 for x in self.sum_hand(d_hand[-1])])
        self.optional_print("\n" + "The dealer's hand is {}. The dealer's score is {}".format(d_hand[0], dealer_score))

        for player in self.players:
            if player.func != dealer_ai:
                self.compare_hands(dealer_score, player)

    def check_cash(self):
        """Print each player's current cash."""
        for player in self.players:
            if player.func != dealer_ai:
                print(f"{player.name} currently has {player.cash}.")

    def reset(self):
        """Reset each player in the game for the next turn."""
        for player in self.players:
            player.reset()


def main():
    my_deck = Deck()
if __name__ == "__main__":
    main()
