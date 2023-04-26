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
    
    result = 0
    result += 20 *state[6]
    result -= 20 *state[13]
    
    result += 6 * state[0]
    result += 5 * state[1]
    result += 4 * state[2]
    result += 3 * state[3]
    result += 2 * state[4]
    result +=  state[5]

    result -= 6 * state[7]
    result -= 5 * state[8]
    result -= 4 * state[9]
    result -= 3 * state[10]
    result -= 2 * state[11]
    result -=  state[12]

    sum_1 = 0 
    for i in range (0,5):
        sum_1 += state[i]

    sum_2 = 0
    for i in range (7,12):
        sum_2 += state[i]

    result += (sum_1 - sum_2) / 6

    if (sum_1 == 0):
      return -100 
    
    if (sum_2 == 0):
      return 100

    # PLACE YOUR CODE HERE
    # result for minimax
    return result
