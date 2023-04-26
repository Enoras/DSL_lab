def func(state: list[int]) -> int:
    """Implementation of minimax strategy

    :param state: list[int]
    state[0, 5] — your pits, state[6] — your kalah
    state[7:12] — opponent's pits, state[13] — opponent's kalah
    :return: int
    result for minimax
    """
    my_pits = state[0:6]
    my_kalah = state[6]
    opp_pits = state[7:13]
    opp_kalah = state[13]

    # Check if the game has ended
    if sum(my_pits) == 0 or sum(opp_pits) == 0:
        return my_kalah - opp_kalah

    # Check if it's my turn
    if sum(my_pits) > sum(opp_pits):
        # Check if I can capture stones from the opponent
        if my_kalah < sum(opp_pits):
            return 100
        # Check if I have more stones than the opponent in my pits
        return 50

    # Check if it's the opponent's turn
    if sum(my_pits) < sum(opp_pits):
        # Check if the opponent has more stones than me in their pits
        return -50

    # Check if it's my turn and if I have stones in my kalah
    if my_kalah > 0:
        return 20

    # Check if I have stones in my pits
    if sum(my_pits) > 0:
        return -20

    # Default case
    return 0
