import blackjack as bj
import statics
import pprint

pp = pprint.PrettyPrinter()

def ML_sim():
    my_perf_ml = bj.AiPlayer("Optimal AI", 500, bj.ml_ai)
    my_perf_ml.set_tables(
        statics.optimal_hard_hands, statics.optimal_soft_hands, statics.optimal_split_hands
    )
    game_master = bj.GameMaster(bj.ml_ai, 500)
    game_master.add_models(100)
    game_master.run_sim(bj.BlackJack, turns=10000, iter=5, deck_num=6,
                        players=[bj.AiPlayer("Dealer", 500, bj.dealer_ai), my_perf_ml])
    pp.pprint(game_master.models[0].hard_table)
    game_master.first_and_last()


def basic_sim():
    my_perf_ml = bj.AiPlayer("Optimal AI", 500, bj.ml_ai)
    dealer = bj.AiPlayer("Dealer", 500, bj.dealer_ai)
    my_perf_ml.set_tables(
        statics.optimal_hard_hands, statics.optimal_soft_hands, statics.optimal_split_hands
    )
    game = bj.BlackJack([my_perf_ml, dealer], deck_num=4, turns=10000, outs = False)
    game.play()
    game.check_cash()
    return game.players

def optimal_tracking():
    results = []
    for x in range(100):
        players = basic_sim()
        for player in players:
            if player.name == "Optimal AI":
                results.append(player.cash)
    print(sum(results)/len(results))
basic_sim()