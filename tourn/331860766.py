def func(state: list[int]) -> float:
    """Implementation of minimax strategy

    :param state: list[int]
        state[0:6] -- your pits, state[6] -- your kalah
        state[7:13] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """

    my_kal = state[6]
    op_kal = state[13]

    my_good = (
        state[0]
        - max(0, state[0] - 6)
        + state[1]
        - max(0, state[1] - 5)
        + state[2]
        - max(0, state[2] - 4)
        + state[3]
        - max(0, state[3] - 3)
        + state[4]
        - max(0, state[4] - 2)
        + state[5]
        - max(0, state[5] - 1)
        + 7
    )

    op_good = (
        state[7]
        - max(0, state[7] - 6)
        + state[8]
        - max(0, state[8] - 5)
        + state[9]
        - max(0, state[9] - 4)
        + state[10]
        - max(0, state[10] - 3)
        + state[11]
        - max(0, state[11] - 2)
        + state[12]
        - max(0, state[12] - 1)
        + 7
    )

    fun = (op_kal + 17.3 / (37 - op_kal) - 40 / op_good) - (
        my_kal + 17.3 / (37 - my_kal) - 40 / my_good
    )

    # return (my_kal - op_kal) * 100 + my_good - op_good
    return fun


# state = [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]
# state0 = [0, 7, 7, 7, 7, 7, 1, 6, 6, 6, 6, 6, 6, 0]
# state1 = [6, 5, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0]
#
# print(func(state0))
# print(func(state1))
