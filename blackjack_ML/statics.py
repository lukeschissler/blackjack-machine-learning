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
