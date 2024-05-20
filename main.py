from source.dealer import Dealer
from source.utility import print_to_file
import os

if __name__ == "__main__":
    output_file = "game_output.txt"
    if os.path.exists(output_file):
        os.remove(output_file)
    print_to_file(f'Initializing match play by initializing Dealer...')
    dealer = Dealer(2, 10, 104, 4, {7:11,9:3})
    print_to_file(f'Match has started, enjoy!')
    dealer.start_match()
    print_to_file(f'Match has completed, thanks for playing!')
