def func(state: list[int]) -> int:
    # Check if game is over
    if not any(state[:6]) or not any(state[8:14]):
        return state[6] - state[13] + sum(state)

    # Find valid moves
    new_state = state[:]
    best_move = 0
    best_score = -float('inf')
    for move, stones in enumerate(state[:6]):
        if stones == 0:
            continue
        new_state[move] = 0
        current_index = move + 1
        while stones > 0:
            current_index %= 14
            if current_index != 13:
                new_state[current_index] += 1
                stones -= 1
            current_index += 1
        score = new_state[6] - new_state[13]
        if score > best_score:
            best_score = score
            best_move = move
            if best_score == sum(state):
                break

    return best_move