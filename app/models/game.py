class Game:
    def __init__(self):
        self.result = None

    def get_winner(self, first_player, second_player):
        if first_player.move == second_player.move:
            return None
        elif first_player.move == "rock" and second_player.move == "paper":
            return first_player
        elif first_player.move == "paper" and second_player.move == "rock":
            return second_player
        elif first_player.move == "rock" and second_player.move == "scissors":
            return first_player
        elif first_player.move == "scissors" and second_player.move == "rock":
            return second_player
        elif first_player.move == "scissors" and second_player.move == "paper":
            return first_player
        elif first_player.move == "paper" and second_player.move == "scissors":
            return second_player
