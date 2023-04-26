# THIS IS TEMPLATE FOR FUNCTION. PLEASE FOLLOW THE RULES:
# 1) Do Not print anything!!!
# 2) Do not exit(0) or smth
# 3) Please do not try to hack us.
def func(state: list[int]) -> int:
    """Implementation of minimax strategy

    :param state: list[int]
        state[0:6] -- your pits, state[6] -- your kalah
        state[8:13] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """
    my_pits = state[:6]
    my_kalah = state[6]
    opp_pits = state[7:13]
    opp_kalah = state[13]

    # Define weights for each of the pits
    pit_weights = [4, 3, 2, 1, 2, 3]

    # Calculate the total score for my pits based on the weights
    my_pit_score = sum([my_pits[i] * pit_weights[i] for i in range(len(my_pits))])

    # Calculate the total score for the opponent's pits based on the weights
    opp_pit_score = sum([opp_pits[i] * pit_weights[i] for i in range(len(opp_pits))])

    # Check if the game has ended
    if sum(my_pits) == 0 or sum(opp_pits) == 0:
        return my_kalah - opp_kalah

    # Check if it's my turn and if I can capture stones from the opponent
    if sum(my_pits) > sum(opp_pits) and my_kalah < sum(opp_pits):
        return 100

    # Check if it's my turn and if I have more stones than the opponent in my pits
    if my_pit_score > opp_pit_score:
        return 50

    # Check if it's my turn and if I have stones in my kalah
    if my_kalah > 0:
        return 20

    # Check if it's the opponent's turn and if they have more stones than me in their pits
    if opp_pit_score > my_pit_score:
        return -50

    # Check if it's the opponent's turn and if I have more stones than them in my pits
    if my_pit_score > opp_pit_score:
        return -20

    # Default case
    return 0