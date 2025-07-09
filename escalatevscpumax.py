import sys
import time
import math

# オセロ盤のサイズ
BOARD_SIZE = 8

# プレイヤー
BLACK = 'B'
WHITE = 'W'
EMPTY = ' '

# 8つの方向
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1), (1, 0), (1, 1)]

# オセロ盤面のクラス
class ReversiBoard:
    def __init__(self):
        self.board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.board[3][3] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[4][4] = WHITE

    def save_board(self, filename):
        with open(filename, 'w') as f:
            for row in self.board:
                f.write(''.join(row) + '\n')

    def display_board(self):
        print('  ' + ' '.join([str(i) for i in range(BOARD_SIZE)]))
        for i in range(BOARD_SIZE):
            print(str(i) + ' ' + ' '.join(self.board[i]))

    def is_valid_move(self, player, x, y):
        if self.board[x][y] != EMPTY:
            return False
        for dx, dy in DIRECTIONS:
            if self._flip_in_direction(player, x, y, dx, dy):
                return True
        return False

    def _flip_in_direction(self, player, x, y, dx, dy):
        flip_positions = []
        nx, ny = x + dx, y + dy
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
            if self.board[nx][ny] == EMPTY:
                break
            if self.board[nx][ny] == player:
                if flip_positions:
                    return flip_positions
                else:
                    break
            flip_positions.append((nx, ny))
            nx += dx
            ny += dy
        return []

    def make_move(self, player, x, y):
        if not self.is_valid_move(player, x, y):
            return False
        self.board[x][y] = player
        for dx, dy in DIRECTIONS:
            flip_positions = self._flip_in_direction(player, x, y, dx, dy)
            for fx, fy in flip_positions:
                self.board[fx][fy] = player
        return True

    def get_valid_moves(self, player):
        valid_moves = []
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if self.is_valid_move(player, x, y):
                    valid_moves.append((x, y))
        return valid_moves

    def is_game_over(self):
        return not self.get_valid_moves(BLACK) and not self.get_valid_moves(WHITE)

    def count_pieces(self):
        black_count = sum(row.count(BLACK) for row in self.board)
        white_count = sum(row.count(WHITE) for row in self.board)
        return black_count, white_count

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

# ゲームのメインループ
def play_game():
    board = ReversiBoard()
    current_player = BLACK
    turn = 0
    while not board.is_game_over():
        board.display_board()
        valid_moves = board.get_valid_moves(current_player)
        if not valid_moves:
            print(f"No valid moves for {current_player}. Skipping turn.")
            current_player = WHITE if current_player == BLACK else BLACK
            continue

        if current_player == BLACK:
            # 人間のターン
            print(f"Your turn ({current_player}).")
            while True:
                try:
                    #駒を最大数取れる場所に置く
                    max_piece = 0
                    max_piece_x = 0
                    max_piece_y = 0
                    for move in valid_moves:
                        new_board = ReversiBoard()
                        new_board.board = [row[:] for row in board.board]
                        new_board.make_move(current_player, *move)
                        black_count, white_count = new_board.count_pieces()
                        if current_player == BLACK:
                            if black_count > max_piece:
                                max_piece = black_count
                                max_piece_x = move[0]
                                max_piece_y = move[1]
                        else:
                            if white_count > max_piece:
                                max_piece = white_count
                                max_piece_x = move[0]
                                max_piece_y = move[1]
                    x, y = max_piece_x, max_piece_y
                    if board.is_valid_move(current_player, x, y):
                        board.make_move(current_player, x, y)
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Enter row and column numbers separated by a space.")
        else:
            # アルゴリズムのターン (Noob)
            print(f"CPU turn ({current_player}).")
            move = noob_move(board, current_player, turn)
            if move:
                board.make_move(current_player, *move)
                turn += 1
            else:
                print("No valid moves for CPU. Skipping turn.")

        current_player = WHITE if current_player == BLACK else BLACK

        # 処理が早いので、ゲームの進行をわかりやすくするために少し待機
        time.sleep(0.5)

    board.display_board()
    black_count, white_count = board.count_pieces()
    if black_count > white_count:
        print("Black wins!")
    elif white_count > black_count:
        print("White wins!")
    else:
        print("It's a tie!")

# ゲーム開始
if __name__ == "__main__":
    play_game()