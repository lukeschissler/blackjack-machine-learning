from random import shuffle, randint

dealer_dict = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'Jack':8, 'Queen':8, 'King': 8,
            'Ace': 9}

hh_dict = {x : y for x, y in zip(reversed([i for i in range(4,21)]), [j for j in range(17)])}

sh_dict  = {x : y for x, y in zip(reversed([i for i in range(2,11)]), [j for j in range(9)])}

sp_dict = {2 : 0, 20:1, 18:2, 16:3, 14:4, 12:5, 10:6, 8:7, 6:8, 4:9}


optimal_hard_hands = [['S','S','S','S','S','S','S','S','S','S'],
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

optimal_soft_hands = [['S','S','S','S','S','S','S','S','S','S'],
              ['S','S','S','S','D','S','S','S','S','S'],
              ['D','D','D','D','D','S','S','H','H','H'],
              ['H','D','D','D','D','H','H','H','H','H'],
              ['H','H','D','D','D','H','H','H','H','H'],
              ['H','H','D','D','D','H','H','H','H','H'],
              ['H','H','H','D','D','H','H','H','H','H'],
              ['H','H','H','D','D','H','H','H','H','H'],
              ['H','H','H','D','D','H','H','H','H','H']]

optimal_split_hands = [['P','P','P','P','P','P','P','P','P','P'],
              ['S','S','S','S','S','S','S','S','S','S'],
              ['P','P','P','P','P','S','P','P','S','S'],
              ['P','P','P','P','P','P','P','P','P','P'],
              ['P','P','P','P','P','P','H','H','H','H'],
              ['P','P','P','P','P','H','H','H','H','H'] ,
              ['D','D','D','D','D','D','D','D','H','H'],
              ['H','H','H','P','P','H','H','H','H','H'],
              ['P','P','P','P','P','P','H','H','H','H'],
              ['P','P','P','P','P','P','H','H','H','H']]


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
        self.func = None

    def __repr__(self) -> str:
        return f"{self.name}: Cash - {self.cash}, Hand - {self.hands}"

    def reset(self) -> None:
        self.antes = []

    def shift_stack(self) -> None:
        self.old_hands.append(self.hands[-1])
        self.hands = self.hands[:-1]
        self.split = 0

class AiPlayer(Player):
    def __init__(self, name, cash, func):
        super().__init__(name, cash)
        self.func = func
        self.fitness_table = []

    def __repr__(self):
        return super().__repr__() + f', Func. - {self.func.__name__}'

    def update_fitness(self, cash):
        self.fitness_table.append(self.cash)
        self.cash = cash

    def set_tables(self, hard_table, soft_table, split_table):
        self.hard_table = hard_table
        self.split_table = split_table
        self.soft_table = soft_table

    def gen_random_tables(self):
        self.hard_table = [[['H', 'S', 'D'][randint(0,2)]for y in range(10)] for x in range(17)]
        self.soft_table = [[['H', 'S', 'D'][randint(0,2)]for y in range(10)] for x in range(9)]
        self.split_table = [[['H', 'S', 'D', 'P'][randint(0,3)]for y in range(10)] for x in range(10)]

    def crossover_tables(self, cross_tables):
        pass

    def mutate(self, mutation_rate):
        pass

class GameMaster:

    def __init__(self):
        self.models = []
        self.used_names = []

    def add_models(self, num, cash, func):
        model_num = randint(0,100000)
        for i in range(num):
            while model_num in self.used_names:
                model_num = randint(0,100000)
            self.used_names.append(model_num)
            player = AiPlayer('Model #'+str(model_num), cash, func)
            player.gen_random_tables()
            self.models.append(player)

    def sort_by_fitness(self, cash):
        for model in self.models:
            model.update_fitness(cash)
        self.models = sorted(self.models, key = lambda x: x.fitness_table[-1])



if __name__ == '__main__':
    my_player = AiPlayer('henry', 500)
    my_player.gen_random_tables()
    print(my_player.hard_table)