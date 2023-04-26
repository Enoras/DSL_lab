# THIS IS TEMPLATE FOR FUNCTION. PLEASE FOLLOW THE RULES:
# 1) Do Not print anything!!!
# 2) Do not exit(0) or smth
# 3) Please do not try to hack us.

def func(state: list[int]) -> float:
    """Implementation of minimax strategy

    :param state: list[int]
        state[0:6] -- your pits, state[6] -- your kalah
        state[8:13] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """

    res = (state[6] - state[13])

    for i in range(0, 6):
        res += -(state[i] - (6 - i)) ** 2 + 6 - i

    for i in range(7, 13):
        res -= -(state[i] - (13 - i)) ** 2 + 13 - i

    return res

if __name__ == "__main__":
    print(func([6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]))