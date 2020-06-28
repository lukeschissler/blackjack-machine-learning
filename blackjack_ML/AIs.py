from statics import hh_dict, sh_dict, sp_dict, dealer_dict


def hand_typer(hand, hand_sums, split):
    """Determines if a hand is soft, split or hard."""
    if 21 in hand_sums:
        return "stand"
    elif len(hand) == 2 and hand[0].return_val() == hand[1].return_val() and not split:
        return "split"
    elif (1, 11) in [x.return_val() for x in hand] and any(j < 10 for j in hand_sums):
        return "soft"
    else:
        return "hard"


def dealer_ai(**kwargs):
    """AI for a dealer. Hits up to hard 16 and on soft 17."""
    hand_sum = kwargs.get("hand_sum")
    if any(j >= 17 and j < 22 for j in hand_sum):
        return "s"
    else:
        return "h"


def ml_ai(**kwargs):
    """AI for ML algorithm. Accepts soft, hard, and split tables and determines move based on hand and dealer's first card."""
    hand_sum = kwargs.get("hand_sum")
    dealer_card = kwargs.get("dealer_card")
    player = kwargs.get("player")
    outs = kwargs.get("outs")

    hand_type = hand_typer(player.hands[-1], hand_sum, player.split)
    if outs:
        print(
            f"Hand: {player.hands[-1]},  hand_type: {hand_type}, D_card: {dealer_card.val}, Ante: {player.antes}"
        )

    if hand_type == "hard":
        return player.hard_table[hh_dict[min(hand_sum)]][
            dealer_dict[dealer_card.val]
        ].lower()
    elif hand_type == "soft":
        return player.soft_table[sh_dict[min(hand_sum)]][
            dealer_dict[dealer_card.val]
        ].lower()
    elif hand_type == "split":
        return player.split_table[sp_dict[min(hand_sum)]][
            dealer_dict[dealer_card.val]
        ].lower()
    else:
        return "s"
