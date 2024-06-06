from source.dealer import Dealer
from source.utility import print_to_file
import os
from json import JSONEncoder

if __name__ == "__main__":
    output_file = "game_output.txt"
    if os.path.exists(output_file):
        os.remove(output_file)

    print_to_file(f'Initializing match play by initializing Dealer...')
    encoder = JSONEncoder()
    params = encoder.encode({
        "match_params" : {
            "number_of_players" : 2,
            "rounds_per_game" : 10,
            "deck_size" : 104,
            "board_size" : 4,
            "card_point_map" : {
                7:11,
                9:3
            }
        }
    })
    dealer = Dealer(params)
    print_to_file(f'Match has started, enjoy!')
    dealer.start_match()
    print_to_file(f'Match has completed, thanks for playing!')
