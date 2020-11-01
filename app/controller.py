import pdb
from flask import render_template, request, redirect
from app import app

from app.models.game import *
from app.models.player import *

player_list = []


@app.route("/")
def index():
    return render_template("index.html", title="home")


@app.route("/one-player")
def one_player():
    return render_template("one-player.html", title="player")


@app.route("/opponent")
def opponent():
    return render_template("opponent.html", title="choose")


@app.route("/choose-opponent", methods=["POST"])
def choose_opponent():
    player_list.clear()
    if request.form["opponent"] == "robot":
        robot_name = "HK-47"
        robot_move = get_robot_move()
        robot_player = Player(robot_name, robot_move)
        player_list.append(robot_player)
        return render_template(
            "one-player.html", title="player", player_list=player_list
        )
    else:
        return render_template(
            "one-player.html", title="player", player_list=player_list
        )


@app.route("/create-player", methods=["POST"])
def create_player():
    winner = None
    player_name = request.form["player-name"]
    player_move = request.form["player-move"]
    player = Player(player_name, player_move)
    player_list.append(player)
    if len(player_list) == 2:
        winner = get_winner(player_list[0], player_list[1])
        return render_template(
            "announce-winner.html",
            player_list=player_list,
            winner=winner,
            title="winner",
        )
    else:
        return render_template(
            "one-player.html", title="player", player_list=player_list
        )
