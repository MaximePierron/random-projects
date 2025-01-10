from extract_colors import rbg_colors
import random
import turtle
from PIL import Image

t = turtle.Turtle()
screen = turtle.Screen()

turtle.colormode(255)
turtle.setup(600, 600)
turtle.bgcolor("cornsilk1")
color_list = rbg_colors
t.speed(9)

t.penup()
t.setheading(180)
t.forward(225)
t.setheading(270)
t.forward(225)
t.setheading(0)
t.pendown()


def u_turn():
    heading = t.heading()
    t.setheading(90)
    t.forward(50)
    if heading == 0:
        t.setheading(180)
    else:
        t.setheading(0)


def draw_dots():
    for _ in range(10):
        for i in range(10):
            t.pendown()
            t.dot(20, random.choice(color_list))
            t.penup()
            if i < 9:
                t.forward(50)
        u_turn()
    t.hideturtle()


screen.listen()
draw_dots()

screen.getcanvas().postscript(file="dots.eps")
dots_img = Image.open("dots.eps")
dots_img.save("dots.png")

screen.exitonclick()
