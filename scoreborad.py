from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Arial", 20, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.game_score_1=0
        self.game_score_2=0
        self.score()

    def score(self):
        self.clear()
        self.color("green")
        self.hideturtle()
        self.penup()
        self.setpos(0,350)
        self.write(f"Player Two's Score: {self.game_score_2}    Player one's Score: {self.game_score_1}",
                   False, ALIGNMENT, FONT)

    def game_over(self, player):
        self.color("green")
        self.hideturtle()
        self.penup()
        self.setpos(0, 0)
        self.write(f"Game over {player}", False, ALIGNMENT, FONT)


    def add_score_1(self):
        self.game_score_1 += 1

    def add_score_2(self):
        self.game_score_2 += 1

