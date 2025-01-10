from turtle import Turtle, Screen

screen = Screen()
screen.listen()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.sety(-255)
        self.move_up()

    def __del__(self):
        pass

    def move_up(self):
        screen.onkey(self.go_up, "Up")

    def go_up(self):
        self.forward(30)

    @staticmethod
    def stop_moving():
        screen.onkey(None, "Up")