import chess
import chess.engine

class ChessGame:
    def __init__(self, difficulty="easy"):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish")  # Stockfishエンジンを使用
        self.difficulty = difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def make_ai_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        self.board.push(result.move)

    def make_player_move(self, move):
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        else:
            return False

    def is_game_over(self):
        return self.board.is_game_over()

    def get_board(self):
        return self.board

    def get_result(self):
        return self.board.result()

    def close_engine(self):
        self.engine.quit()