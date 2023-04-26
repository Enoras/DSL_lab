# THIS IS TEMPLATE FOR FUNCTION. PLEASE FOLLOW THE RULES:
# 1) Do Not print anything!!!
# 2) Do not exit(0) or smth
# 3) Please do not try to hack us.


def func(state: list[int]) -> int:
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
        state[i] += new_state[i]

    state[6] *= 5
    state[13] *= 5
    state[6] += sum([state[i] >= 6 - i for i in range(6)])
    state[13] += sum([state[i] >= 13 - i for i in range(7, 13)])

    return state[6] - state[13]
