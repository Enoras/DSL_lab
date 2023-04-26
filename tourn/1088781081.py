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
    # result for minimax
    i = 0
    sum1 = 0
    while i <= 6:
        sum1+=state[i]
        i+=1
    i = 7
    sum2 = 0
    while i <= 12:
        sum2+=state[i]
        i+=1
    return (state[6]-state[13])*100+sum1-sum2
