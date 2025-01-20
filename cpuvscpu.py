import sys
import time

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

# ミニマックス法を使用したCPUの思考アルゴリズム
def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or board.is_game_over():
        black_count, white_count = board.count_pieces()
        return black_count - white_count

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.get_valid_moves(BLACK):
            new_board = ReversiBoard()
            new_board.board = [row[:] for row in board.board]
            new_board.make_move(BLACK, *move)
            eval = minimax(new_board, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.get_valid_moves(WHITE):
            new_board = ReversiBoard()
            new_board.board = [row[:] for row in board.board]
            new_board.make_move(WHITE, *move)
            eval = minimax(new_board, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board, player, depth):
    best_move = None
    best_eval = float('-inf') if player == BLACK else float('inf')
    for move in board.get_valid_moves(player):
        new_board = ReversiBoard()
        new_board.board = [row[:] for row in board.board]
        new_board.make_move(player, *move)
        eval = minimax(new_board, depth - 1, player == WHITE, float('-inf'), float('inf'))
        if player == BLACK and eval > best_eval:
            best_eval = eval
            best_move = move
        elif player == WHITE and eval < best_eval:
            best_eval = eval
            best_move = move
    return best_move

# ゲームのメインループ
def play_game():
    board = ReversiBoard()
    current_player = BLACK

    while not board.is_game_over():
        board.display_board()
        valid_moves = board.get_valid_moves(current_player)

        if not valid_moves:
            print(f"No valid moves for {current_player}. Skipping turn.")
            current_player = WHITE if current_player == BLACK else BLACK
            continue

        if current_player == BLACK:
            print(f"CPU ({current_player})'s turn.")
            move = find_best_move(board, current_player, depth=1)
            if move:
                board.make_move(current_player, *move)
            else:
                print("No valid moves for CPU. Skipping turn.")
        else:
            # CPUのターン
            print(f"CPU ({current_player})'s turn.")
            move = find_best_move(board, current_player, depth=6)
            if move:
                board.make_move(current_player, *move)
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