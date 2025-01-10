from turtle import Turtle


class Highway(Turtle):
    STARTING_Y = -240
    STARTING_X = -350

    def __init__(self):
        super().__init__()
        self.penup()
        self.sety(self.STARTING_Y)
        self.setx(self.STARTING_X)
        self.pendown()
        self.number_of_lane = 16
        self.draw_highway()

    def draw_highway(self):
        for i in range(0, self.number_of_lane+1):
            if i % 2 == 0:
                self.setheading(0)
            else:
                self.setheading(180)
            self.draw_lane()
            self.setheading(90)
            self.forward(30)

    def draw_lane(self):
        for i in range(70):
            if i % 2 == 0:
                self.penup()
            else:
                self.pendown()
            self.forward(10)

