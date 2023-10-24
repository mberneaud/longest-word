"""Module that provides the Game class used to play the game"""
import random
import string
import requests
import json

class Game: # pylint: disable=too-few-public-methods
    """Game that asks users to create the longest possible word using 9 letters"""
    def __init__(self) -> None:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid and it's a valid English word"""

        # Check word against le Wagons dictionary API
        url = f"https://wagon-dictionary.herokuapp.com/{word}"
        r = requests.get(url)
        r = json.loads(r.text)
        if r["found"] is False:
            return False

        # initiate counter for valid letters and a copy of the game grid
        valid_counter = 0
        grid_queue = self.grid

        for letter in word:
            if letter in grid_queue:  # if letter is found in grid copy
                valid_counter += 1  # increment counter and
                grid_queue.remove(letter)  # remove letter from grid copy

        return len(word) == valid_counter
