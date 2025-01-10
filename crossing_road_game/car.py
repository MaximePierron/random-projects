from turtle import Turtle, Screen
from random import choice, randint

import static

COLOR_LIST = ["green", "yellow", "blue", "red", "orange"]
screen = Screen()
screen.tracer(0)


class Car(Turtle):
    def __init__(self, lane=0):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.set_color()
        self.sety(-225)
        self.setx(315)

    def __del__(self):
        pass

    def set_color(self):
        self.color(choice(COLOR_LIST))

    @staticmethod
    def set_lane():
        lane_number = randint(0, 15)
        return lane_number

    def go_to_lane(self, lane_number):
        self.sety(-225 + lane_number * 30)

    def move(self):
        self.forward(10)
        if self.xcor() <= -325:
            del self
