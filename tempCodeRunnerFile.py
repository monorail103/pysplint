def noob_move(board, player, turn):
    advantages = []
    for move in board.get_valid_moves(player):
        new_board = ReversiBoard()
        new_board.board = [row[:] for row in board.board]
        advantage = 0
        for dx, dy in DIRECTIONS:
            advantage += len(new_board._flip_in_direction(player, move[0], move[1], dx, dy))
        advantages.append(advantage)
        result = math.floor(len(advantages) * turn / 60)
    print(f"{turn}ターン目")
    if len(board.get_valid_moves(player)) == 0:
        return None
    return board.get_valid_moves(player)[result]