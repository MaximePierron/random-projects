import time
import turtle

turtle.tracer(False)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.penup()
        self.color("white")
        self.hot = True
        self.sleep_time = 0.05

    def __del__(self):
        pass

    def start(self, left=True):
        self.setx(0)
        self.sety(0)
        self.sleep_time = 0.05
        time.sleep(1)
        if left:
            self.setheading(135)
            self.move()
            return 135
        else:
            self.setheading(45)
            self.move()
            return 45

    def move(self):
        self.forward(10)
        time.sleep(self.sleep_time)
        turtle.update()
        if self.ycor() >= 285:
            if 90 <= self.heading() <= 270:
                self.setheading(self.heading() + 90)
            else:
                self.setheading(self.heading() - 90)
            self.move()
        if self.ycor() <= -285:
            if 90 <= self.heading() <= 270:
                self.setheading(self.heading() - 90)
            else:
                self.setheading(self.heading() + 90)
            self.move()

    def go_off_screen(self):
        start_time = time.time()
        seconds = 2.
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            self.move()
            if elapsed_time > seconds:
                break
