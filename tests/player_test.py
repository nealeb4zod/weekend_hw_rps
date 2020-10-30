import unittest

from app.models.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Emilia", "rock")

    def test_player_name(self):
        self.assertEqual("Emilia", self.player_1.name)

    def test_player_move(self):
        self.assertEqual("rock", self.player_1.move)