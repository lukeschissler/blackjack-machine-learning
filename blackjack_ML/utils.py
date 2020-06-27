from random import shuffle, randint, random

"""X-value corresponding to the dealer's first card."""
dealer_dict = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "10": 8,
    "Jack": 8,
    "Queen": 8,
    "King": 8,
    "Ace": 9,
}

"""Y value corresponding to the AI's hand when hand_type = hard"""
hh_dict = {
    x: y for x, y in zip(reversed([i for i in range(4, 21)]), [j for j in range(17)])
}

"""Y-value corresponding to the AI's hand when hand_type = soft."""
sh_dict = {
    x: y for x, y in zip(reversed([i for i in range(2, 11)]), [j for j in range(9)])
}

"""Y-Value corresponding to the AI'shand when hand_type = split."""
sp_dict = {2: 0, 20: 1, 18: 2, 16: 3, 14: 4, 12: 5, 10: 6, 8: 7, 6: 8, 4: 9}

"""Table for the optimal hard hands."""
optimal_hard_hands = [
    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
    ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
    ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
    ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
    ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
    ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],
    ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
    ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],
    ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
]

"""Table for the optimal soft hands.  """
optimal_soft_hands = [
    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
    ["S", "S", "S", "S", "D", "S", "S", "S", "S", "S"],
    ["D", "D", "D", "D", "D", "S", "S", "H", "H", "H"],
    ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
    ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
    ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
    ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
    ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
    ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
]

"""Table for the optimal split hands."""
optimal_split_hands = [
    ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P"],
    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
    ["P", "P", "P", "P", "P", "S", "P", "P", "S", "S"],
    ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P"],
    ["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"],
    ["P", "P", "P", "P", "P", "H", "H", "H", "H", "H"],
    ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],
    ["H", "H", "H", "P", "P", "H", "H", "H", "H", "H"],
    ["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"],
    ["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"],
]


class Card:
    """Card  type object. Consists of a value and a suit."""

    def __init__(self, val: str, suit: str) -> None:
        """Initialize a card with a val. and suit"""
        self.val = val
        self.suit = suit

    def __repr__(self) -> str:
        """Customize the representation of the card class."""
        return f"{self.val} of {self.suit}"

    def return_val(self):
        """Translate a card's value to it's numerical value. Aces can be 1 or 11."""
        if self.val in ["King", "Jack", "Queen", "10"]:
            return "10"
        elif self.val in "Ace":
            return (1, 11)
        else:
            return self.val


class Deck:
    """The Deck object,which is a collection of Card objects. """
    def __init__(self, num=1) -> None:
        """Initialize  a deck with the size of deck required. """
        self.num = num
        self.deck_reset()

    def deck_reset(self) -> None:
        """Reset a deck and add as many times as you need."""
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        vals = [str(x) for x in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
        self.deck = [Card(x, y) for x in vals for y in suits] * self.num

    def shuffle(self) -> None:
        """Shuffle the deck."""
        shuffle(self.deck)

    def deal(self, size) -> list:
        """Implement more true to life deal"""
        return [self.deck.pop() for x in range(size)]


class Player:
    """Player object for the blackjack game."""
    def __init__(self, name, cash):
        """Initialize a player with its name, cash, hands, antes, split and optional func. Func is the AI that will play."""
        self.name = name
        self.cash = cash
        self.hands = []
        self.played_hands = []
        self.antes = []
        self.split = 0
        self.func = None

    def __repr__(self) -> str:
        """Customzie the outstring for the Player class."""
        return f"{self.name}: Cash - {self.cash}, Hand - {self.hands}"

    def reset(self) -> None:
        """Reset a player for a new hand."""
        self.played_hands = []
        self.antes = []
        self.split = 0

    def shift_stack(self) -> None:
        """Move a hand off the current stack to the out_stack."""
        self.played_hands.append(self.hands[-1])
        self.hands = self.hands[:-1]

    def split_turn(self, ante) -> None:
        self.split = 1
        self.antes.append(ante)
        self.cash -= ante

    def double_down_turn(self, ante) -> None:
        self.cash -= ante
        self.antes[-1] += ante
        self.shift_stack()

    def stand_turn(self) -> None:
        self.shift_stack()


class AiPlayer(Player):
    """Child class of player with more attr and methods to support an AI player"""
    def __init__(self, name, cash, func):
        super().__init__(name, cash)
        self.func = func
        self.fitness_table = []

    def __repr__(self):
        """Customize the outstring of the class."""
        return f"{self.name}, Fitness: {self.fitness_table}, Cash: {self.cash}"

    def update_fitness(self, c):
        """Update fitness table with current generation's cash."""
        self.fitness_table.append(self.cash)
        self.cash = c

    def set_tables(self, hard_table, soft_table, split_table):
        """Manually enter tables for AI logic"""
        self.hard_table = hard_table
        self.split_table = split_table
        self.soft_table = soft_table

    def gen_random_tables(self):
        """Generate random tables to initialize AI"""
        self.hard_table = [
            [["H", "S", "D"][randint(0, 2)] for y in range(10)] for x in range(17)
        ]
        self.soft_table = [
            [["H", "S", "D"][randint(0, 2)] for y in range(10)] for x in range(9)
        ]
        self.split_table = [
            [["H", "S", "D", "P"][randint(0, 3)] for y in range(10)] for x in range(10)
        ]

    def mutate(self, mutation_rate):
        """Unimplemented. Iterate through tables and alter value according to preset mutation rate."""
        pass


class GameMaster:
    """GameMaster class. Handles gameplay for multiple AIs, crossing over between generations."""
    def __init__(self, func, cash):
        self.models = []
        self.used_names = []
        self.cash = cash
        self.func = func

    def add_models(self, num):
        """Add models to the game master."""
        model_num = randint(0, 100000)
        for i in range(num):
            while model_num in self.used_names:
                model_num = randint(0, 100000)
            self.used_names.append(model_num)
            player = AiPlayer("Model #" + str(model_num), self.cash, self.func)
            player.gen_random_tables()
            self.models.append(player)

    def update_fitness(self):
        """For each model, update its fitness table with the current generation's winnings"""
        for model in self.models:
            model.update_fitness(self.cash)

    def crossover(self, p1, p2):
        """Crossover two parent models to generate a child model. Genetic content from each parent based on fitness ratio between parents."""
        p1_fitness = p1.fitness_table[-1]
        p2_fitness = p2.fitness_table[-1]
        p1_ratio = 1 - abs(p1_fitness) / (abs(p1_fitness) + abs(p2_fitness)+1)
        child_hhs = [[] for x in range(17)]
        child_shs = [[] for x in range(9)]
        child_phs = [[] for x in range(10)]

        for x in range(17):
            for p1s, p2s in zip(p1.hard_table[x], p2.hard_table[x]):
                if random() < p1_ratio:
                    child_hhs[x].append(p1s)
                else:
                    child_hhs[x].append(p2s)

        for x in range(9):
            for p1s, p2s in zip(p1.soft_table[x], p2.soft_table[x]):
                if random() < p1_ratio:
                    child_shs[x].append(p1s)
                else:
                    child_shs[x].append(p2s)

        for x in range(10):
            for p1s, p2s in zip(p1.split_table[x], p2.split_table[x]):
                if random() < p1_ratio:
                    child_phs[x].append(p1s)
                else:
                    child_phs[x].append(p2s)

        child = AiPlayer(str(randint(0, 1000000)), self.cash, self.func)
        child.set_tables(child_hhs, child_shs, child_phs)
        if p1_fitness > p2_fitness:
            child.fitness_table += p1.fitness_table
        else:
            child.fitness_table += p2.fitness_table
            # child.name = p2.name

        return child

    def select_parent(self):
        """Select a parent from two potential models based on fitness from a randomly-sized population."""
        p1 = randint(0, len(self.models) - 1)
        p2 = randint(0, len(self.models) - 1)
        if self.models[p1].fitness_table[-1] > self.models[p2].fitness_table[-1]:
            return p1
        else:
            return p2

    def tournament_selection(self, ratio = 1):
        """Cross two parents over to generate a child table. Define a ratio of children from the previous generation and newly generated models."""

        old_len = len(self.models)
        children = []
        while len(children) < len(self.models) * ratio:
            parent_1 = self.models[self.select_parent()]
            parent_2 = self.models[self.select_parent()]
            child = self.crossover(parent_1, parent_2)
            children.append(child)

        self.models = children
        while old_len > len(self.models) :
            self.add_models(1)


    def first_and_last(self):
        """Return the first and last fitness measurement for each model in the object."""
        for model in self.models:
            print(f"Model: {model.name}, First: {model.fitness_table[0]} Last: {model.fitness_table[-1]}")

    def run_sim(self, game, turns, iter, deck_num, players = []):


        for i in range(iter):
            for model in self.models:
                simulation = game(players + [model], deck_num, turns=turns, ante=50)

                simulation.play()

            self.update_fitness()
            self.tournament_selection(1)



if __name__ == "__main__":
    pass
