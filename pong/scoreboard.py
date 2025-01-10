from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score(0, 0)

    def update_score(self, score_player1, score_player2):
        self.clear()
        self.goto(0, 215)
        self.write(f"SCORE:\n{score_player2} : {score_player1}",
                   False,
                   align="center",
                   font=("Courier", 30, "normal")
                   )
