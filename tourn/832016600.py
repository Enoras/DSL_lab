def pos(state: list[int], ind) -> int:
    if ind < 6:
        if state[ind] < 6 - ind:
            return 1
        else:
            return -(state[ind] - (6 - ind))
    else:
        if state[ind] < 13 - ind:
            return 1
        else:
            return -(state[ind] - (13 - ind))

def func(state: list[int]) -> int:
    """Implementation of minimax strategy

    :param state: list[int]
        state[0:6] -- your pits, state[6] -- your kalah
        state[7:13] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """

    k1 = state[6]
    k2 = state[13]

    s1 = sum([pos(state,i) for i in range(0,5)])
    s2 = sum([pos(state,i) for i in range(7,12)])

    e1 = sum([1 for i in range(0,5) if state[i] == 0])
    e2 = sum([1 for i in range(7,12) if state[i] == 0])

    score = k1 - k2
    score += (s1 - s2)*0.2
    score += (e2 - e1)*0.1

    return score
