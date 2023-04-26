def func(state: list[int]) -> float:
    A = state[0] + state[1] + state[2] + state[3] + state[4] + state[5]
    B = state[7] + state[8] + state[9] + state[10] + state[11] + state[12]

    return ((state[6] + 19.5 / (37 - state[6]) - (36 - A)) - (state[13] + 19.5 / (37 - state[13]) - (36 - B)))
