import turtle
import time

turtle.tracer(False)
screen = turtle.Screen()
screen.listen()


class Paddle(turtle.Turtle):
    def __init__(self, action_button_up, action_button_down, starting_x_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.color("white")
        self.penup()
        self.action_button_up = action_button_up
        self.action_button_down = action_button_down
        self.starting_x_cor = starting_x_cor
        self.position_paddle()
        self.up = True
        self.move_paddle()

    def __del__(self):
        pass

    def position_paddle(self):
        self.speed(0)
        self.goto(self.starting_x_cor, 0)

    def move_paddle(self):
        screen.onkey(self.go_up, self.action_button_up)
        screen.onkey(self.go_down, self.action_button_down)

    def go_up(self):
        self.setheading(90)
        time.sleep(0.001)
        self.forward(20)
        turtle.update()

    def go_down(self):
        self.setheading(270)
        time.sleep(0.001)
        self.forward(20)
        turtle.update()
