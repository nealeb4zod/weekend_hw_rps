from flask import render_template, request, redirect
from app import app

from app.models.players import *


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/mvp")
def mvp():
    return render_template("mvp.html", title="Home")


@app.route("/choose", methods=["POST"])
def choose_the_winner():
    player_1_name = request.form["p1name"]
    player_1_move = request.form["p1move"]
    player_2_name = request.form["p2name"]
    player_2_move = request.form["p2move"]
    player_1 = Player(player_1_name, player_1_move)
    player_2 = Player(player_2_name, player_2_move)
    return announce_winner(get_winner(player_1, player_2))


@app.route("/<move_1>/<move_2>")
def who_won(move_1, move_2):
    first_player = get_player_from_move(move_1)
    second_player = get_player_from_move(move_2)
    announce_winner(get_winner(player_1, player_2))
