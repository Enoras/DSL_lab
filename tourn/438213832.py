# def func(state):
#     p1_kalah = state[6]
#     p2_kalah = state[13]
    
#     p1_side = sum(state[0:6])
#     p2_side = sum(state[7:13])

#     opp_side = p2_side

#     p1_empty = sum([1 for i in range(6) if state[i] == 0])
#     p2_empty = sum([1 for i in range(7, 13) if state[i] == 0])

#     center = sum(state[1:6])

#     score = p1_kalah - p2_kalah
#     score += (p1_side - p2_side) * 0.2
#     score += (opp_side - p1_side) * 0.2
#     score += (p1_empty - p2_empty) * 0.1
#     score += center * 0.3
#     return score

def func(state):
    return (state[6] - state[13]) + sum(state[0:6]) - sum(state[7:13])
