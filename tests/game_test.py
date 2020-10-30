import unittest

from app.models.player import Player
from app.models.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Emilia", "rock")
        self.player_2 = Player("Tom", "paper")
        self.player_3 = Player("Rosie", "scissors")
        self.game = Game()

    # possible outcomes:

    # same = draw
    # rock/paper = paper wins
    # paper/rock = paper wins
    # rock/scissors = rock wins
    # scissors/rock = rock wins
    # scissors/paper = scissors wins
    # paper/scissors = scissors wins

    # same = draw
    def test_rock_rock(self):
        winner = self.game.get_winner(self.player_1, self.player_1)
        self.assertEqual(None, winner)

    def test_paper_paper(self):
        winner = self.game.get_winner(self.player_2, self.player_2)
        self.assertEqual(None, winner)

    def test_scissors_scissors(self):
        winner = self.game.get_winner(self.player_1, self.player_1)
        self.assertEqual(None, winner)

    # rock/paper = paper wins
    def test_rock_paper(self):
        winner = self.game.get_winner(self.player_1, self.player_2)
        self.assertEqual(self.player_1, winner)

    # paper/rock = paper wins
    def test_paper_rock(self):
        winner = self.game.get_winner(self.player_2, self.player_1)
        self.assertEqual(self.player_1, winner)

    # rock/scissors = rock wins
    def test_rock_scissors(self):
        winner = self.game.get_winner(self.player_1, self.player_3)
        self.assertEqual(self.player_1, winner)

    # scissors/rock = rock wins
    def test_scissors_rock(self):
        winner = self.game.get_winner(self.player_3, self.player_1)
        self.assertEqual(self.player_1, winner)

    # scissors/paper = scissors wins
    def test_scissors_paper(self):
        winner = self.game.get_winner(self.player_3, self.player_2)
        self.assertEqual(self.player_3, winner)

    # paper/scissors = scissors wins
    def test_paper_scissors(self):
        winner = self.game.get_winner(self.player_2, self.player_3)
        self.assertEqual(self.player_3, winner)