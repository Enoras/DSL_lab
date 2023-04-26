def func(state: list[int]) -> float:
    """
    Evaluate the current state of the game and return a score for the given player.
    """
    player = 0
    opponent = (player % 2) + 1  # determine the opponent's player number
    score = 0
    
    # Calculate the difference in the number of stones each player has captured
    player_score = state[6]
    opponent_score = state[13]
    score += player_score - opponent_score
    
    # Add a bonus for having more stones in the Kalah
    kalah_bonus = 0
    if player_score > opponent_score:
        kalah_bonus = player_score - opponent_score
    elif player_score < opponent_score:
        kalah_bonus = -opponent_score + player_score
    score += kalah_bonus
    
    # Add a penalty for having empty pits on the player's side of the board
    empty_penalty = 0
    for i in range(6):
        if state[i] == 0:
            empty_penalty -= 2
    score += empty_penalty
    
    # Add a bonus for having more stones on the opponent's side of the board
    opponent_side_bonus = 0
    for i in range(6):
        if state[i+7] > 0:
            opponent_side_bonus += state[i+7]
    score += opponent_side_bonus
    
    # Add a penalty for having fewer stones on the player's side of the board than the opponent
    side_stones_penalty = 0
    for i in range(6):
        if state[i] < state[i+7]:
            side_stones_penalty -= state[i+7] - state[i]
    score += side_stones_penalty
    
    return score