# THIS IS TEMPLATE FOR FUNCTION. PLEASE FOLLOW THE RULES:
# 1) Do Not print anything!!!
# 2) Do not exit(0) or smth
# 3) Please do not try to hack us.


def func(state: list[int]) -> int:
    """Implementation of minimax strategy

    :param state: list[int]
        state[0:6] -- your pits, state[6] -- your kalah
        state[7:13] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """
    # if state[5] == 1:
    #     return state[6] + 1
    # if state[4] == 2:
    #     return state[6] + 2
    # if state[3] == 3:
    #     return state[6] + 3
    # if state[2] == 4:
    #     return state[6] + 4
    # if state[1] == 5:
    #     return state[6] + 5
    # if state[0] == 6:
    #     return state[6] + 6
    # return state[13] - state[6]
    temp = 0

    for i in range(0, 7):
        temp += state[i]

    if state[0] <= 6:
        return state[6] + 1
    elif state[1] <= 5:
        return state[6] + 1
    elif state[2] <= 4:
        return state[6] + 1
    elif state[3] <= 3:
        return state[6] + 1
    elif state[4] <= 2:
        return state[6] + 1
    elif state[5] <= 1:
        return state[6] + 1

    return state[6] + temp / 13
