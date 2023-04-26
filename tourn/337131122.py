def func(state):
  # player: the player who the evaluation is being done for (either 0 or 1)

  # Calculate the total number of seeds on each side of the board
  player_seeds = sum(state[:6])
  opponent_seeds = sum(state[7:13])

  # Calculate the difference in seeds between the two sides
  seed_diff = player_seeds - opponent_seeds

  # Calculate the number of empty houses on each side of the board
  player_empty = sum([1 for i in range(6) if state[i] == 0])
  opponent_empty = sum([1 for i in range(7, 13) if state[i] == 0])

  # Calculate the difference in empty houses between the two sides
  empty_diff = player_empty - opponent_empty

  # Calculate the mobility of each player
  player_moves = [i for i in range(6) if state[i] != 0]
  opponent_moves = [i for i in range(7, 13) if state[i] != 0]
  mobility_diff = len(player_moves) - len(opponent_moves)

  # Combine all the factors to calculate the overall score
  score = seed_diff + empty_diff + mobility_diff

  return score