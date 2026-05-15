import unittest
import connect4

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.board = connect4.create_board()

    # Happy path tests
    def test_create_start_board(self):
        self.assertEqual(self.board.shape, (6, 7))
        self.assertTrue((self.board == 0).all())

    def test_drop_piece_places_piece_correctly(self):
        connect4.drop_piece(self.board, 0, 0, 1)
        self.assertEqual(self.board[0, 0], 1)

    def test_horizontal_win_detection(self):
        for c in range(4):
            connect4.drop_piece(self.board, 0, c, 1)

        self.assertTrue(connect4.winning_move(self.board, 1))
        self.assertFalse(connect4.winning_move(self.board, 2))

    def test_vertical_win_detection(self):
        for r in range(4):
            connect4.drop_piece(self.board, r, 0, 1)

        self.assertTrue(connect4.winning_move(self.board, 1))
        self.assertFalse(connect4.winning_move(self.board, 2))

    # Validation tests
    def test_full_column_move_rejected(self):
        for r in range(6):
            connect4.drop_piece(self.board, r, 0, 1)
        self.assertFalse(connect4.is_valid_location(self.board, 0))

    # Edge-case tests
    def test_last_available_row_in_column(self):
        for r in range(5):
            connect4.drop_piece(self.board, r, 0, 1)
        self.assertEqual(connect4.get_next_open_row(self.board, 0), 5)

    def test_three_in_row_is_not_win(self):
        for c in range(3):
            connect4.drop_piece(self.board, 0, c, 1)
        self.assertFalse(connect4.winning_move(self.board, 1))


if __name__ == "__main__":
    unittest.main()