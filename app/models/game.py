from random import choice


def get_winner(first_player, second_player):
    if first_player.move == second_player.move:
        return None
    elif first_player.move == "paper" and second_player.move == "rock":
        return first_player
    elif first_player.move == "rock" and second_player.move == "scissors":
        return first_player
    elif first_player.move == "scissors" and second_player.move == "paper":
        return first_player
    else:
        return second_player


def get_robot_move():
    moves = ["rock", "paper", "scissors"]
    return choice(moves)