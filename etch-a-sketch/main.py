import turtle

t = turtle.Turtle()
s = turtle.Screen()

turtle.setup(800, 800)
turtle.bgcolor("DarkSeaGreen1")

s.listen()


def draw_right():
    t.forward(10)


def draw_left():
    t.backward(10)


def rotate_left():
    heading = t.heading()
    t.setheading(heading+5)


def rotate_right():
    heading = t.heading()
    t.setheading(heading-5)


s.onkey(draw_right, "Right")
s.onkey(draw_left, "Left")
s.onkey(rotate_right, "Down")
s.onkey(rotate_left, "Up")

s.exitonclick()
