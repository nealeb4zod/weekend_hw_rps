from flask import render_template, request, redirect
from random import choice

from app import app
from app.models.game import *
from app.models.player import Player

game = Game()
print(game.first_player, game.second_player)


@app.route("/")
def index():
    game = Game()
    return render_template("index.html", title="home", game=game)


@app.route("/one-player")
def one_player():
    return render_template("one-player.html", title="player")


@app.route("/opponent")
def opponent():
    game = Game()
    return render_template("opponent.html", title="choose", game=game)


@app.route("/choose-opponent", methods=["POST"])
def choose_opponent():
    game = Game()
    print(game.first_player, game.second_player)
    if request.form["opponent"] == "robot":
        robot_name = "HK-47"
        robot_move = choice(["rock", "paper", "scissors"])
        robot_player = Player(robot_name, robot_move)
        game.add_player_to_game(robot_player)
        return render_template("one-player.html", title="player", game=game)
    else:
        return render_template("one-player.html", title="player", game=game)


@app.route("/create-player", methods=["POST"])
def create_player():
    print(game.first_player, game.second_player)
    player_name = request.form["player-name"]
    player_move = request.form["player-move"]
    player = Player(player_name, player_move)
    game.add_player_to_game(player)
    if game.first_player is not None and game.second_player is not None:
        game.winner = game.get_winner()
        player_list = [game.first_player, game.second_player]
        return render_template(
            "announce-winner.html",
            player_list=player_list,
            winner=game.winner,
            title="winner",
        )
    else:
        return render_template("one-player.html", title="player", game=game)
