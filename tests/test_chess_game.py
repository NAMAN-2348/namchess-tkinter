import unittest

from chess_game import ChessGame, Piece


class ChessGameTests(unittest.TestCase):
    def setUp(self) -> None:
        self.game = ChessGame()

    def test_initial_piece_count(self) -> None:
        count = sum(1 for row in self.game.board for piece in row if piece is not None)
        self.assertEqual(count, 32)

    def test_pawn_has_one_or_two_step_from_start(self) -> None:
        moves = set(self.game.legal_moves((6, 4)))
        self.assertEqual(moves, {(5, 4), (4, 4)})

    def test_knight_can_jump(self) -> None:
        moves = set(self.game.legal_moves((7, 1)))
        self.assertEqual(moves, {(5, 0), (5, 2)})

    def test_turn_changes_after_valid_move(self) -> None:
        moved = self.game.move((6, 4), (4, 4))
        self.assertTrue(moved)
        self.assertEqual(self.game.current_turn, "black")

    def test_cannot_move_wrong_color(self) -> None:
        self.assertFalse(self.game.move((1, 4), (3, 4)))

    def test_bishop_moves_after_clearing_path(self) -> None:
        self.assertTrue(self.game.move((6, 3), (4, 3)))
        self.assertTrue(self.game.move((1, 0), (2, 0)))
        moves = set(self.game.legal_moves((7, 2)))
        self.assertIn((6, 3), moves)
        self.assertIn((5, 4), moves)

    def test_pawn_capture(self) -> None:
        game = ChessGame()
        game.board = [[None for _ in range(8)] for _ in range(8)]
        game.board[4][4] = Piece("white", "pawn")
        game.board[3][5] = Piece("black", "knight")
        moves = set(game.legal_moves((4, 4)))
        self.assertIn((3, 5), moves)


if __name__ == "__main__":
    unittest.main()
