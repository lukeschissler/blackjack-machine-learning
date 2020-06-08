from random import shuffle
from AIs import dealer_ai


class Card:
    def __init__(self, val: str, suit: str) -> None:
        self.val = val
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.val} of {self.suit}"

    def return_val(self):
        if self.val in ['King', 'Jack', 'Queen', '10']:
            return '10'
        elif self.val in 'Ace':
            return (1,11)
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
        self.score_card = []
        self.ante = 0
        self.split = 0

    def __repr__(self):
        return f'{self.name}: Cash - {self.cash}, Hand - {self.hands}'

class BlackJack:
    def __init__(self, players, deck_num=1, turns=1, cash = 500, ante=50, double_down = 0) -> None:
        self.players = [Player(x, cash) for x in players]
        self.deck_num = deck_num
        self.ais = [dealer_ai]
        self.turns = turns
        self.deck = Deck(deck_num)
        self.ante = ante
        self.double_down = double_down

    def deal(self) -> None:
        if len(self.deck.deck) < len(self.players) + 52:
            self.deck.deck_reset()
            self.deck.shuffle()
        else:
            for player in self.players:
                player.hands.append(self.deck.deal(2))

    def sum_hand(self, hand) -> list:
        sums = [0]

        for card in hand:
            if card.val in ["Jack", "Queen", "King"]:
                sums = [x + 10 for x in sums]
            elif card.val == "Ace":
                sums = [x + 1 for x in sums] + [x + 11 for x in sums]
            else:
                sums = [x + int(card.val) for x in sums]
        return sorted(set(sums))

    def turn(self, player) -> None:
        print(f"Your hand is: {player.hands[-1]}. Possible sums: {self.sum_hand(player.hands[-1])}")
        player.ante = [self.ante]
        player.cash -= self.ante
        hit, dd, hands, player.split = 0, 0, [-1], 0

        if player.hands[-1][0].return_val() == player.hands[-1][1].return_val():
            split = int(input("Split? (0/1): "))
            if split:
                player.hands += [[player.hands[-1][0]] +self.deck.deal(1), [player.hands[-1][1]]+self.deck.deal(1)]
                player.ante = [self.ante, self.ante]
                player.cash -= self.ante
                player.split = 1
                hands = [-2, -1]

        for h in hands:

            if player.split:
                print(f"Your hand is: {player.hands[h]}. Possible sums: {self.sum_hand(player.hands[h])}")

            if self.double_down:
                dd = int(input("Double down? (0/1): "))
                if dd:
                    player.ante[h] += self.ante
                    player.cash -= self.ante


            while True:

                if not dd:
                    hit = int(input("Hit? (0/1): "))

                if hit or dd:
                    player.hands[h] += self.deck.deal(1)
                    hand_sum = self.sum_hand(player.hands[h])
                else:
                    break

                if 21 in hand_sum:
                    print(f"{player.name}\'s hand is: {player.hands[h]}. Your sum is 21.")
                    break
                elif all(j > 21 for j in hand_sum):
                    print(f"{player.name}\'s hand is {player.hands[h]}. You busted at {hand_sum}")
                    break
                elif dd:
                    print(f"{player.name}\'s hand is: {player.hands[h]}, sum: {hand_sum}. You double-downed and cannot hit again.")
                    break
                else:
                    print(f"{player.name}\'s hand is: {player.hands[h]}. Possible sums: {hand_sum}")

            hand_sums = [x for x in self.sum_hand(player.hands[h]) if x < 22]

            if not hand_sums:
                player.score_card.append(0)
            else:
                player.score_card.append(max(hand_sums))


    def ai_play(self, ai_player) -> None:
        while True:

            hit = ai_player.name(self.sum_hand(ai_player.hands[-1]))

            if hit:
                ai_player.hands[-1] += self.deck.deal(1)
                hand_sum = self.sum_hand(ai_player.hands[-1])
            else:
                break

            if 21 in hand_sum or all(j > 21 for j in hand_sum):
                break
            else:
                pass

        hand_sums = [x for x in self.sum_hand(ai_player.hands[-1]) if x < 22]

        if not hand_sums:
            ai_player.score_card.append(0)
        else:
            ai_player.score_card.append(max(hand_sums))


    def play(self) -> None:
        self.deck.shuffle()
        for i in range(self.turns):
            print('\n'+'It\'s a new deal!')
            self.deal()

            for player in self.players:
                if player.name in self.ais:
                    self.ai_play(player)
                else:
                    self.turn(player)

            self.assess()
            self.check_cash()


    def assess(self) -> str:

        for player in self.players:
            if player.name == dealer_ai:
                dealer_score = player.score_card[-1]
                print('\n'+f'The dealer\'s hand is {player.hands[-1]}. The dealer\'s score is {dealer_score}')


        for player in self.players:
            hands = [-1]

            if player.split:
                hands = [-2, -1]
            if player.name not in self.ais:
                for h in hands:
                    if player.score_card[h] == 0:
                        print(f'{player.name} busted with {player.score_card[h]} and lost {player.ante[h]}')
                    elif player.score_card[h] == dealer_score:
                        player.cash += sum(player.ante)
                        print(f'{player.name} tied dealer with {player.score_card[h]} and made back their ante of {player.ante[h]}')
                    elif player.score_card[h] < dealer_score:
                        print(f'{player.name} lost to the dealer with {player.score_card[h]} and lost {player.ante[h]}')
                    else:
                        player.cash += sum(player.ante) * 2
                        print(f'{player.name} won with {player.score_card[h]} and made {player.ante[h]*2}')

    def check_cash(self):
        for player in self.players:
            if player.name not in self.ais:
                print(f'{player.name} currently has {player.cash}.')

def main():
    print(dealer_ai in [dealer_ai])
    game = BlackJack(['Tim', 'Brad', dealer_ai], deck_num=4, turns=100)
    game.play()

if __name__ == "__main__":
    main()
