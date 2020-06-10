from AIs import dealer_ai, hits_ai, dd_ai, ml_ai
from utils import Deck, Player

class BlackJack:
    def __init__(self, players, deck_num=1, turns=1, cash=500, ante=50) -> None:
        self.players = [Player(x, cash) for x in players]
        self.deck_num = deck_num
        self.turns = turns
        self.deck = Deck(deck_num)
        self.ante = ante

    def deal(self) -> None:
        if len(self.deck.deck) < len(self.players) + 52:
            self.deck.deck_reset()
            self.deck.shuffle()

        for player in self.players:
            player.hands.append(self.deck.deal(2))
            player.antes.append(self.ante)

    def dealer_hand(self, state) -> list:
        for player in self.players:
            if player.name == dealer_ai:
                if state == "curr":
                    return player.hands
                if state == "old":
                    return player.old_hands

    def sum_hand(self, hand) -> list:
        sums = [0]

        for card in hand:
            if card.val == "Ace":
                sums = [x + 1 for x in sums] + [x + 11 for x in sums]
            else:
                sums = [x + int(card.return_val()) for x in sums]
        return sorted(set(sums))

    def turn(self, player: Player) -> None:
        player.cash -= self.ante
        player.antes.append(self.ante)

        while player.hands:
            if callable(player.name):
                move = player.name(
                    hand_sum=self.sum_hand(player.hands[-1]),
                    dealer_card=self.d1_card,
                    hand=player.hands[-1],
                    split=player.split
                )
                print(str(player.name)+' -> '+move)
                if len(player.hands[-1]) > 2 and move == 'd':
                    move = 'h'
            else:
                print(
                    f"It's {player.name}'s turn. Hand: {player.hands[-1]}. Sum(s): {self.sum_hand(player.hands[-1])}"
                )
                move = input("Split (P), Double-Down (D), Hit (H), Stand (S): ").lower()

            if move == "p" and len(player.hands) == 1:
                if player.hands[-1][0].return_val() == player.hands[-1][1].return_val():
                    player.split = 1
                    player.antes.append(self.ante)
                    player.cash -= self.ante
                    player.hands = [
                        [player.hands[-1][0]] + self.deck.deal(1),
                        [player.hands[-1][1]] + self.deck.deal(1),
                    ]
                else:
                    print(
                        "You cannot split because your cards do not have the same value."
                    )

            elif move == "d":
                if len(player.hands[-1]) == 2:
                    player.hands[-1] += self.deck.deal(1)
                    player.cash -= self.ante
                    player.antes[-1] += self.ante
                    player.shift_stack()
                else:
                    print("You cannot double down after the first hit.")

            elif move == "h":
                player.hands[-1] += self.deck.deal(1)

            elif move == "s":
                player.shift_stack()

            else:
                print("Enter a valid move next time.")

            if player.hands:
                hand_sum = self.sum_hand(player.hands[-1])
                if 21 in hand_sum or all(j > 21 for j in hand_sum):
                    player.shift_stack()
                else:
                    pass

    def play(self) -> None:
        self.deck.shuffle()
        for i in range(self.turns):
            print("\n" + "It's a new deal!")
            self.deal()
            self.d1_card = self.dealer_hand('curr')[0][0]

            for player in self.players:
                self.turn(player)

            self.settlement()
            self.check_cash()
            self.reset()

    def settlement(self):

        d_hand = self.dealer_hand("old")
        dealer_sums = [x if x < 22 else 0 for x in self.sum_hand(d_hand[-1])]
        if not dealer_sums:
            dealer_score = 0
        else:
            dealer_score = max(dealer_sums)

        print(
            "\n"
            + "The dealer's hand is {}. The dealer's score is {}".format(
                d_hand[0], dealer_score
            )
        )

        for player in self.players:
            if player.name == dealer_ai:
                player.old_hands = player.old_hands[:-1]

            if player.name != dealer_ai:
                while player.old_hands:
                    hand_sum = self.sum_hand(player.old_hands[-1])
                    if all(j > 21 for j in hand_sum):
                        score = 0
                    else:
                        score = max(hand_sum)

                    if score == 0:
                        print(
                            f"{player.name} busted with {score} and lost {player.antes[-1]}"
                        )
                    elif score == dealer_score:
                        player.cash += player.antes[-1]
                        print(
                            f"{player.name} tied dealer with {score} and made back their ante of {player.antes[-1]}"
                        )
                    elif score < dealer_score:
                        print(
                            f"{player.name} lost to the dealer with {score} and lost {player.antes[-1]}"
                        )
                    else:
                        player.cash += player.antes[-1] * 2
                        print(
                            f"{player.name} won with {score} and made {player.antes[-1]*2}"
                        )
                    player.antes = player.antes[:-1]
                    player.old_hands = player.old_hands[:-1]

    def check_cash(self):
        for player in self.players:
            if player.name != dealer_ai:
                print(f"{player.name} currently has {player.cash}.")

    def reset(self):
        for player in self.players:
            player.reset()


def main():
    game = BlackJack([dealer_ai, ml_ai, hits_ai, dd_ai], deck_num=4, turns=3000)
    game.play()


if __name__ == "__main__":
    main()
