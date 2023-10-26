from longest_word.game import Game
import string
import random

# tests/test_game.py
class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()
        # grid init
        grid = game.grid
        # verify types
        assert type(grid) == list
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        # verify
        assert new_game.is_valid('') == (False, 0)

    def test_is_valid(self):
        random.seed(42)
        new_game = Game() # initiates grid to ['U', 'D', 'A', 'X', 'I', 'H', 'H', 'E', 'X']
        assert new_game.is_valid("AXE") == (True, 3)

    def test_is_invalid(self):
        random.seed(42)
        new_game = Game() # initiates grid to ['U', 'D', 'A', 'X', 'I', 'H', 'H', 'E', 'X']
        assert new_game.is_valid("DAISY") == (False, 0)

    def test_unkown_word2_is_invalid(self):
        random.seed(42)
        new_game = Game() # initiates grid to ['U', 'D', 'A', 'X', 'I', 'H', 'H', 'E', 'X']
        assert new_game.is_valid("DAXI") == (False, 0)

    def test_unknown_word_is_invalid(self):
        """A word that == not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') == (False, 0)
