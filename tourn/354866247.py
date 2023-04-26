# THIS IS TEMPLATE FOR FUNCTION. PLEASE FOLLOW THE RULES:
# 1) Do Not print anything!!!
# 2) Do not exit(0) or smth
# 3) Please do not try to hack us.


# def func(state: list[int]) -> float:
#     """Implementation of minimax strategy

#     :param state: list[int]
#         state[0:6] -- your pits, state[6] -- your kalah
#         state[8:13] -- opponent's pits, state[13] -- opponent's kalah
#     :return: int
#         result for minimax
#     """
#     player_kalah = 6
#     opp_kalah = 13
#     player_holes = state[:6]
#     opp_holes = state[7:13]
#     if sum(player_holes) == 0:
#         return 100 - state[opp_kalah]
#     if sum(opp_holes) == 0:
#         return state[player_kalah] - 100
#     kalah_diff = state[player_kalah] - state[opp_kalah]
#     holes_diff = sum(player_holes) - sum(opp_holes)
#     rate = kalah_diff + holes_diff
#     return rate


# def func(state: list[int]) -> float:
#     """Implementation of minimax strategy

#     :param state: list[int]
#         state[0:6] -- your pits, state[6] -- your kalah
#         state[8:13] -- opponent's pits, state[13] -- opponent's kalah
#     :return: int
#         result for minimax
#     """
#     return (state[6] - state[-1]) * 100 + sum(state[:6]) - sum(state[7:13])


def func(state: list[int]) -> float:
    """Implementation of minimax strategy

    :param state: list[int]
        state[0:6] -- your pits, state[6] -- your kalah
        state[8:13] -- opponent's pits, state[13] -- opponent's kalah
    :return: int
        result for minimax
    """
    player = 0
    own_holes = state[:6]
    own_kalah = state[6]
    opp_holes = state[7:13]
    opp_kalah = state[13]

    if player == 0:
        score = own_kalah - opp_kalah
    else:
        score = opp_kalah - own_kalah

    stones_on_board = sum(own_holes) + own_kalah + sum(opp_holes) + opp_kalah
    if stones_on_board == 0:
        return score

    stones_per_hole = stones_on_board // 12
    if stones_per_hole == 0:
        stones_per_hole = 1

    for i in range(6):
        stones = own_holes[i]
        if stones == 0:
            continue
        end_hole = (i + stones) % 14
        if end_hole == 6 and player == 1:
            continue
        if end_hole == 13 and player == 0:
            continue
        if end_hole < 6:
            if own_holes[end_hole] == 0 and opp_holes[5-end_hole] != 0:
                score -= stones_per_hole
        elif end_hole == 6:
            score += stones_per_hole
        else:
            if opp_holes[12-end_hole] == 0 and own_holes[11-end_hole] != 0:
                score += stones_per_hole

    return score

    return score


# print(list(i for i in range(14)))
# print(func(list(i for i in range(14))))