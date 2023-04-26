# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def func(state: list[int]) -> int:
    p1_kalah = state[6]
    p2_kalah = state[13]

    p1_side = sum(state[0:6])
    p2_side = sum(state[7:13])

    opp_side = p2_side

    p1_empty = sum([1 for i in range(6) if state[i] == 0])
    p2_empty = sum([1 for i in range(7, 13) if state[i] == 0])

    center = sum(state[1:6])

    score = p1_kalah - p2_kalah
    score += (p1_side - p2_side) * 0.2
    score += (opp_side - p1_side) * 0.2
    score += (p1_empty - p2_empty) * 0.1
    score += center * 0.3
    """Implementation of minimax strategy

    :param state: list[int]
        state[0:6] -- your pits, state[6] -- your kalah
        state[8:13] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """

    # PLACE YOUR CODE HERE
    # result for minimax
    return score