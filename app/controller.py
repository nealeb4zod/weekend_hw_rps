from flask import render_template, request, redirect
from app import app


from app.models.players import *


@app.route("/")
def index():
    return render_template("index.html", title="home")


@app.route("/two-players")
def two_players():
    return render_template("two-players.html", title="players")


@app.route("/one-player")
def one_player():
    return render_template("one-player.html", title="player")


@app.route("/choose-opponent", methods=["POST"])
def choose_opponent():
    if request.form["opponent"] == "human":
        return render_template("two-players.html", title="players")
    else:
        return render_template("one-player.html", title="players")


@app.route("/create-players", methods=["POST"])
def create_players():
    player_1_name = request.form["p1name"]
    player_1_move = request.form["p1move"]
    player_2_name = request.form["p2name"]
    player_2_move = request.form["p2move"]
    player_1 = Player(player_1_name, player_1_move)
    player_2 = Player(player_2_name, player_2_move)
    player_list.append(player_1)
    player_list.append(player_2)
    winner = get_winner(player_1, player_2)
    return render_template(
        "announce-winner.html", player_list=player_list, winner=winner
    )


@app.route("/create-player1", methods=["POST"])
def create_player1():
    player_list = []
    winner = None
    player_1_name = request.form["p1name"]
    player_1_move = request.form["p1move"]
    robot_name = "Randy Robot"
    robot_move = get_robot_move()
    player_1 = Player(player_1_name, player_1_move)
    player_2 = Player(robot_name, "paper")
    player_list.append(player_1)
    player_list.append(player_2)
    winner = get_winner(player_1, player_2)
    return render_template(
        "announce-winner.html", player_list=player_list, winner=winner
    )
