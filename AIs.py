from random import random

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
              ['H','H','H','H','H','H','H','H','H','H']]


def random_ai():
    return round(random())


def dealer_ai(**kwargs):
    hand_sum = kwargs.get("hand_sum")
    if any(j >= 18 and j < 22 for j in hand_sum):
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


def ml_ai(hh_table, **kwargs):
    hand_sum = kwargs.get('hand_sum')
    dealer_card = kwargs.get('dealer_card')
    hand = kwargs.get('hand')




def main():
    print(random_ai())


if __name__ == "__main__":
    main()
