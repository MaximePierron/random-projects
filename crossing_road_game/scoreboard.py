from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-215, 255)
        self.write(f"Level: {self.level}", False, align="center", font=("Courier", 15, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Courier", 30, "normal"))