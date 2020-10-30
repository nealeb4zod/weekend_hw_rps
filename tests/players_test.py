import unittest

from app.models.players import *
from app.models.player import Player
from app.models.game import Game


class TestPlayers(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Emilia", "rock")
        self.player_2 = Player("Tom", "paper")
        self.player_3 = Player("Rosie", "scissors")
        self.game = Game()

    def test_get_player_from_rock(self):
        player = get_player_from_move("rock")
        self.assertEqual(self.player_1, player)

    def test_get_player_from_paper(self):
        player = get_player_from_move("paper")
        self.assertEqual(self.player_2, player)

    def test_get_player_from_scissors(self):
        player = get_player_from_move("scissors")
        self.assertEqual(self.player_3, player)