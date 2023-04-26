# THIS IS TEMPLATE FOR FUNCTION. PLEASE FOLLOW THE RULES:
# 1) Do Not print anything!!!
# 2) Do not exit(0) or smth
# 3) Please do not try to hack us.


def func(state: list[int]) -> int:
    """Implementation of minimax strategy

    :param state: list[int]
        state[0:5] -- your pits, state[6] -- your kalah
        state[7:12] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """
    p1_kalah = state[6]
    p2_kalah = state[13]

    p1_side = sum(state[0:6])
    p2_side = sum(state[7:13])

    opp_side = p2_side

    p1_empty = sum([1 for i in range(6) if state[i] == 0])
    p2_empty = sum([1 for i in range(7, 13) if state[i] == 0])

    center = sum(state[1:6])

    score = p1_kalah - p2_kalah
    score += (p1_side - p2_side) * 0.2
    score += (opp_side - p1_side) * 0.2
    score += (p1_empty - p2_empty) * 0.1
    score += center * 0.3

    return score
