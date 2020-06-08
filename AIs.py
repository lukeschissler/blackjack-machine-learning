from random import random

def random_ai():
    return round(random())

def dealer_ai(hand_sum):
    if max(hand_sum) >= 17:
        return 0
    else:
        return 1


def bad_ai():
    pass


def decent_ai():
    pass


def perfect_ai():
    pass


def main():
    print(random_ai())


if __name__ == "__main__":
    main()
