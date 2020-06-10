from random import random

def random_ai():
    return round(random())

def dealer_ai(**kwargs):
    hand_sum = kwargs.get('hand_sum')
    if max(hand_sum) >= 17:
        return 's'
    else:
        return 'h'


def hits_ai():
    pass


def decent_ai():
    pass


def perfect_ai():
    pass


def main():
    print(random_ai())


if __name__ == "__main__":
    main()
