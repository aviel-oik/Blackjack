def ask_player_action() -> str:
    valid_input = False
    while not valid_input:
        choose = input('Enter H to draw a card and S to pass : ')
        if choose == 'H' or choose == 'S':
            valid_input = True
        else:
            print('Invalid input')
    return choose

