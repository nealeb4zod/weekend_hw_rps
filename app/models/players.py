import pdb

from app.models.player import Player


from app.models.game import Game


player_1 = Player("Emilia", "rock")
player_2 = Player("Tom", "paper")
player_3 = Player("Rosie", "scissors")
game = Game()

# pass in two moves
#     get player for move1
#     get player for move2
#     get winner of players


def get_player_from_move(move):
    for player in [player_1, player_2, player_3]:
        if move == player.move:
            return player
