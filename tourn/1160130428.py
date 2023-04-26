def func(state):
    my_kalah = state[6]
    opponent_kalah = state[13]
    my_stones = sum(state[:6])
    opponent_stones = sum(state[7:13])
    score = my_kalah - opponent_kalah + my_stones - opponent_stones
    return score