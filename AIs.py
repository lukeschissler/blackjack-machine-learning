from random import random

dealer_dict = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'Jack':8, 'Queen':8, 'King': 8,
            'Ace': 9}

hh_dict = {x : y for x, y in zip(reversed([i for i in range(4,21)]), [j for j in range(17)])}

sh_dict  = {x : y for x, y in zip(reversed([i for i in range(2,11)]), [j for j in range(9)])}

sp_dict = {2 : 0, 20:1, 18:2, 16:3, 14:4, 12:5, 10:6, 8:7, 6:8, 4:9}


hard_hands = [['S','S','S','S','S','S','S','S','S','S'],
              ['S','S','S','S','S','S','S','S','S','S'],
              ['S','S','S','S','S','S','S','S','S','S'],
              ['S','S','S','S','S','S','S','S','S','S'],
              ['S','S','S','S','S','H','H','H','H','H'],
              ['S','S','S','S','S','H','H','H','H','H'],
              ['S','S','S','S','S','H','H','H','H','H'],
              ['S','S','S','S','S','H','H','H','H','H'],
              ['H','H','S','S','S','H','H','H','H','H'],
              ['D','D','D','D','D','D','D','D','D','D'],
              ['D','D','D','D','D','D','D','D','H','H'],
              ['H','D','D','D','D','H','H','H','H','H'],
              ['H','H','H','H','H','H','H','H','H','H'],
              ['H','H','H','H','H','H','H','H','H','H'],
              ['H','H','H','H','H','H','H','H','H','H'],
              ['H','H','H','H','H','H','H','H','H','H'],
              ['H','H','H','H','H','H','H','H','H','H']]

soft_hands = [['S','S','S','S','S','S','S','S','S','S'],
              ['S','S','S','S','D','S','S','S','S','S'],
              ['D','D','D','D','D','S','S','H','H','H'],
              ['H','D','D','D','D','H','H','H','H','H'],
              ['H','H','D','D','D','H','H','H','H','H'],
              ['H','H','D','D','D','H','H','H','H','H'],
              ['H','H','H','D','D','H','H','H','H','H'],
              ['H','H','H','D','D','H','H','H','H','H'],
              ['H','H','H','D','D','H','H','H','H','H']]

split_hands = [['P','P','P','P','P','P','P','P','P','P'],
              ['S','S','S','S','S','S','S','S','S','S'],
              ['P','P','P','P','P','S','P','P','S','S'],
              ['P','P','P','P','P','P','P','P','P','P'],
              ['P','P','P','P','P','P','H','H','H','H'],
              ['P','P','P','P','P','H','H','H','H','H'] ,
              ['D','D','D','D','D','D','D','D','H','H'],
              ['H','H','H','P','P','H','H','H','H','H'],
              ['P','P','P','P','P','P','H','H','H','H'],
              ['P','P','P','P','P','P','H','H','H','H']]

def hand_typer(hand, hand_sums, split):
    if len(hand) == 2 and hand[0].return_val() == hand[1].return_val() and not split:
        return 'split'
    elif (1, 11) in [x.return_val() for x in hand] and any(j < 10 for j in hand_sums):
        return 'soft'
    else:
        return 'hard'

def random_ai():
    return round(random())


def dealer_ai(**kwargs):
    hand_sum = kwargs.get("hand_sum")
    if any(j >= 17 and j < 22 for j in hand_sum):
        return "s"
    else:
        return "h"


def hits_ai(**kwargs):
    return "h"


def dd_ai(**kwargs):
    hand = kwargs.get('hand')
    if len(hand) == 2:
        if random() > 0.5:
            return 'd'
    return 'h'


def ml_ai(**kwargs):
    hand_sum = kwargs.get('hand_sum')
    dealer_card = kwargs.get('dealer_card')
    hand = kwargs.get('hand')
    split = kwargs.get('split')

    hand_type = hand_typer(hand, hand_sum, split)
    print(f'Hand: {hand},  hand_type: {hand_type}, D_card: {dealer_card.val}')

    if hand_type == 'hard':
        return hard_hands[hh_dict[min(hand_sum)]][dealer_dict[dealer_card.val]].lower()
    elif hand_type == 'soft':
        return soft_hands[sh_dict[min(hand_sum)]][dealer_dict[dealer_card.val]].lower()
    else:
        return split_hands[sp_dict[min(hand_sum)]][dealer_dict[dealer_card.val]].lower()


def main():
    print(hh_dict)


if __name__ == "__main__":
    main()
