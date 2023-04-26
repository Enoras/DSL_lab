def func(state: list[int]) -> int:
    state[6] *= 3
    state[13] *= 3

    new_state = [0 for i in range(14)]

    for i in range(6):
        alpha = state[i] - 6 + i
        if 0 < alpha < 8:
            for j in range(7, 7 + alpha):
                new_state[j] += 1

    for i in range(7, 13):
        alpha = state[i] - 13 + i
        if 0 < alpha < 8:
            for j in range(alpha):
                new_state[j] += 1

    for i in range(14):
        state[i] += new_state[i] // 2

    state[6] += sum([state[i] >= 6 - i for i in range(6)])
    state[13] += sum([state[i] >= 13 - i for i in range(7, 13)])

    return state[6] - state[13]
