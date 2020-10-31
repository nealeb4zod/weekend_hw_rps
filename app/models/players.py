from app.models.player import Player
from random import randint

player_list = []
winner = None


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


def get_robot_move():
    move_number = randint(1, 3)
    if move_number == 1:
        return "rock"
    elif move_number == 2:
        return "paper"
    elif move_number == 3:
        return "scissors"