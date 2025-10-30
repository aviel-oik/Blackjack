from core import player_io

def calculate_hand_value(hand: list[dict]) -> int:
    total_value = 0
    for card in hand:
        if card['rank'] == 'A':
            total_value += 1
        elif card['rank'] == 'K' or card['rank'] == 'Q' or card['rank'] == 'J':
            total_value += 10
        else:
            total_value += int(card['rank'])
    return total_value



def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player['hand'].append(deck.pop(0))
    player['hand'].append(deck.pop(0))
    dealer['hand'].append(deck.pop(0))
    dealer['hand'].append(deck.pop(0))
    print(f"dealer value : {dealer['hand'][0]['rank']} + {dealer['hand'][1]['rank']} = {calculate_hand_value(dealer['hand'])}")
    print(f"player value : {player['hand'][0]['rank']} + {player['hand'][1]['rank']} = {calculate_hand_value(player['hand'])}")



def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer['hand']) <= 17:
        dealer['hand'].append(deck.pop(0))
    print(f"dealer value : {calculate_hand_value(dealer['hand'])}")
    if calculate_hand_value(dealer['hand']) > 21:
        print('The dealer went over 21 \nthe dealer lost !')
        return False
    else:
        return True



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    another_player_session = True
    while another_player_session:
        choose = player_io.ask_player_action()
        player_not_lost = True
        if choose == 'H':
            player['hand'].append(deck.pop(0))
            value = calculate_hand_value(player['hand'])
            print(f"the card drawn by the player is : {player['hand'][-1]['rank']}")
            print(f"player value : {value}")
            if value > 21:
                print('The player went over 21 \nthe player lost !')
                another_player_session = False
                player_not_lost = False
        if choose == 'S':
            another_player_session = False
            dealer_not_lost = dealer_play(deck, dealer)
    if player_not_lost and dealer_not_lost:
        player_value = calculate_hand_value(player['hand'])
        dealer_value = calculate_hand_value(dealer['hand'])
        print(f"player value : {player_value}")
        if player_value > dealer_value:
            print("The total value of the player's cards is higher than that of the dealer \nThe player win !")
        if dealer_value > player_value:
            print("The total value of the dealer's cards is higher than that of the player \nThe dealer win !")
        else:
            print('Both players reached the same score, \ndraw!')



