# Re-importing the necessary classes and constants from the user's provided code
# Recreating necessary parts of the Reversi game logic to compute actual scores
import matplotlib.pyplot as plt


# Constants
BOARD_SIZE = 8
BLACK = 'B'
WHITE = 'W'
EMPTY = ' '

# Directions for flipping pieces
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1), (1, 0), (1, 1)]

# Reversi board class
class ReversiBoard:
    def __init__(self):
        self.board = [
            [WHITE, WHITE, WHITE, BLACK, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, WHITE, BLACK, WHITE, EMPTY, EMPTY, EMPTY, EMPTY],
            [BLACK, WHITE, BLACK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, BLACK, WHITE, BLACK, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, BLACK, WHITE, BLACK, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, BLACK, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        ]

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

    def count_pieces(self):
        black_count = sum(row.count(BLACK) for row in self.board)
        white_count = sum(row.count(WHITE) for row in self.board)
        return black_count, white_count

    def evaluate_board(self):
        # Evaluate based on the difference in pieces
        black_count, white_count = self.count_pieces()
        return black_count - white_count

    def generate_evaluation_scores(self, player):
        scores = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if self.is_valid_move(player, x, y):
                    temp_board = ReversiBoard()
                    temp_board.board = [row[:] for row in self.board]
                    temp_board.board[x][y] = player
                    scores[x][y] = temp_board.evaluate_board()
                else:
                    scores[x][y] = None  # Invalid move
        return scores

# Create an instance of the board
board = ReversiBoard()

# Generate evaluation scores for black
scores = board.generate_evaluation_scores(BLACK)

# Visualize the evaluation scores
def visualize_board_with_evaluations(board, scores, title="Othello Evaluation with Valid Moves"):
    fig, ax = plt.subplots(figsize=(8, 8))

    # Draw the board grid
    for x in range(9):
        ax.plot([0, 8], [x, x], color="black", linewidth=0.5)
        ax.plot([x, x], [0, 8], color="black", linewidth=0.5)

    # Add scores as heatmap-like text
    for x in range(8):
        for y in range(8):
            cell_color = "white" if board.board[x][y] == EMPTY else ("black" if board.board[x][y] == BLACK else "gray")
            score = scores[x][y]
            if score is not None:
                ax.text(y + 0.5, 7.5 - x, f"{score:.1f}",
                        ha="center", va="center", fontsize=18, color="red")
            if board.board[x][y] != EMPTY:
                ax.add_patch(plt.Circle((y + 0.5, 7.5 - x), 0.4, color=cell_color, ec="black"))

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_xticks(range(9))
    ax.set_yticks(range(9))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect('equal')
    ax.set_title(title, fontsize=16)
    plt.show()

# Visualize the board with evaluations
visualize_board_with_evaluations(board, scores, title="Evaluation Scores (Black's Turn)")
