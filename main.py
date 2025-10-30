from core import deck
from core import game_logic

def main():
    if __name__ == "__main__":
        deck_not_mixed = deck.build_standard_deck()
        deck_mixed = deck.shuffle_by_suit(deck_not_mixed)
        player = {'hand' : []}
        dealer = {'hand' : []}
        game_logic.run_full_game(deck_mixed, player, dealer)

main()