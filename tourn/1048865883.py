# THIS IS TEMPLATE FOR FUNCTION. PLEASE FOLLOW THE RULES:
# 1) Do Not print anything!!!
# 2) Do not exit(0) or smth
# 3) Please do not try to hack us.


def func(state: list[int]) -> int:
    result = (state[6] - state[13])*2

    hole_count_me = 0
    hole_count_opponent = 0 
    # количество пустый лунок моих и оппонента
    for h in state[0:6]:
        if h == 0:
            hole_count_me += 1

    for h in state[7:13]:
        if h == 0:
            hole_count_opponent += 1

    # количество таких ходов, в которых можно не пополнять лунку оппонента
    for i in range(0,6):
        if state[i] + i <= 6 and state[i] != 0:
            result += 2

    for i in range(7,13):
        if state[i] + i <= 13 and state[i] != 0:
            result -= 1

    result += hole_count_opponent - hole_count_me

    """Implementation of minimax strategy

    :param state: list[int]
        state[0:6] -- your pits, state[6] -- your kalah
        state[8:13] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """

    # PLACE YOUR CODE HERE
    # result for minimax
    return result
