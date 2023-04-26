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

    # PLACE YOUR CODE HERE
    max = 0
    copy = 0
    N = len(state)
    for i in range (N):
        if state[i] > max:
            max = state[i]
        else:
            if state[i] == max:
                copy = max

    if max == 6:
        if state[max + 1] > state[max - 1]:
            max = max + 1
        else:
            max = max - 1

    if max == 13:
        max = max - 1

    if max > 6:
        max = 14 - max



    # result for minimax
    return max
