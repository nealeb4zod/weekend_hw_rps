from app.models.player import Player

player_1 = Player("Emilia", "rock")
player_2 = Player("Tom", "paper")
player_3 = Player("Rosie", "scissors")


def get_player_from_move(move):
    for player in [player_1, player_2, player_3]:
        if move == player.move:
            return player


def get_winner(first_player, second_player):
    if first_player.move == second_player.move:
        return None
    elif first_player.move == "rock" and second_player.move == "paper":
        return second_player
    elif first_player.move == "paper" and second_player.move == "rock":
        return first_player
    elif first_player.move == "rock" and second_player.move == "scissors":
        return first_player
    elif first_player.move == "scissors" and second_player.move == "rock":
        return second_player
    elif first_player.move == "scissors" and second_player.move == "paper":
        return first_player
    elif first_player.move == "paper" and second_player.move == "scissors":
        return second_player


def announce_winner(winner):
    if winner is None:
        return "It's a draw!"
    else:
        return f" {winner.name}  won!"
