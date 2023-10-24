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

    def test_is_valid(self):
        random.seed(42)
        new_game = Game() # initiates grid to ['U', 'D', 'A', 'X', 'I', 'H', 'H', 'E', 'X']
        assert new_game.is_valid("AXE") == True

    def test_is_invalid(self):
        random.seed(42)
        new_game = Game() # initiates grid to ['U', 'D', 'A', 'X', 'I', 'H', 'H', 'E', 'X']
        assert new_game.is_valid("DAISY") == False
