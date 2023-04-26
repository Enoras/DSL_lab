# THIS IS TEMPLATE FOR FUNCTION. PLEASE FOLLOW THE RULES:
# 1) Do Not print anything!!!
# 2) Do not exit(0) or smth
# 3) Please do not try to hack us.


def func(state: list[int]):
    """Implementation of minimax strategy

    :param state: list[int]
        state[0:6] -- your pits, state[6] -- your kalah
        state[7:13] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """
    K_a = state[6]
    K_b = state[13]
    D_a = sum(state[0:6])
    D_b = sum(state[7:13])
    W = (K_a - K_b) * 100 + (D_a - D_b)
    return W
