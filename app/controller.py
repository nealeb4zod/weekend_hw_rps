from flask import render_template
from app import app
from app.models.players import get_player_from_move
import app.models.game


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/<move_1>/<move_2>")
def who_won(move_1, move_2):
    first_player = get_player_from_move(move_1)
    second_player = get_player_from_move(move_2)
    app.models.game.get_winner(first_player, second_player)