def check_finish(player1, player2):
    player1_sum = player1.sum()
    player2_sum = player2.sum()

    if player2_sum == 21:
        return 'player2'
    elif player1_sum > 21:
        return 'player2'
    elif player1_sum == 21:
        return 'player1'
    elif player2_sum > 21:
        return 'player1'

    return None