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

    n = 0
    for i in range(6):
        n += state[i]
    if (n > 18) & (n < 24) and state[6] >= state[13]:
        return state[6] - state[13]
    else:
        return 0

    
