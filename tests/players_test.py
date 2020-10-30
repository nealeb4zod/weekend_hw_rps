import unittest

from app.models.players import *
from app.models.player import Player


class TestPlayers(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Emilia", "rock")
        self.player_2 = Player("Tom", "paper")
        self.player_3 = Player("Rosie", "scissors")

    def test_get_player_from_rock(self):
        player = get_player_from_move("rock")
        self.assertEqual(self.player_1, player)

    def test_get_player_from_paper(self):
        player = get_player_from_move("paper")
        self.assertEqual(self.player_2, player)

    def test_get_player_from_scissors(self):
        player = get_player_from_move("scissors")
        self.assertEqual(self.player_3, player)

    def test_rock_rock(self):
        winner = get_winner(self.player_1, self.player_1)
        self.assertEqual(None, winner)

    def test_paper_paper(self):
        winner = get_winner(self.player_2, self.player_2)
        self.assertEqual(None, winner)

    def test_scissors_scissors(self):
        winner = get_winner(self.player_1, self.player_1)
        self.assertEqual(None, winner)

    # rock/paper = paper wins
    def test_rock_paper(self):
        winner = get_winner(self.player_1, self.player_2)
        self.assertEqual(self.player_2, winner)

    # paper/rock = paper wins
    def test_paper_rock(self):
        winner = get_winner(self.player_2, self.player_1)
        self.assertEqual(self.player_2, winner)

    # rock/scissors = rock wins
    def test_rock_scissors(self):
        winner = get_winner(self.player_1, self.player_3)
        self.assertEqual(self.player_1, winner)

    # scissors/rock = rock wins
    def test_scissors_rock(self):
        winner = get_winner(self.player_3, self.player_1)
        self.assertEqual(self.player_1, winner)

    # scissors/paper = scissors wins
    def test_scissors_paper(self):
        winner = get_winner(self.player_3, self.player_2)
        self.assertEqual(self.player_3, winner)

    # paper/scissors = scissors wins
    def test_paper_scissors(self):
        winner = get_winner(self.player_2, self.player_3)
        self.assertEqual(self.player_3, winner)