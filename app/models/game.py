class Game:
    def __init__(self):
        self.first_player = None
        self.second_player = None
        self.winner = None

    def get_winner(self):
        if self.first_player.move == self.second_player.move:
            self.winner = None
        elif self.first_player.move == "paper" and self.second_player.move == "rock":
            self.winner = self.first_player
        elif self.first_player.move == "rock" and self.second_player.move == "scissors":
            self.winner = self.first_player
        elif (
            self.first_player.move == "scissors" and self.second_player.move == "paper"
        ):
            self.winner = self.first_player
        else:
            self.winner = self.second_player
        return self.winner

    def add_player_to_game(self, player):
        if self.first_player == None:
            self.first_player = player
        elif self.second_player == None:
            self.second_player = player
