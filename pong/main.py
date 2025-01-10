import turtle as t
from paddle import Paddle
from ball import Ball
from mediator import PongMediator
from scoreboard import Scoreboard


screen = t.Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The famous game of Pong")


paddle1 = Paddle("Up", "Down", 350)
paddle2 = Paddle("w", "s", -350)
ball = Ball()
scoreboard = Scoreboard()

mediator = PongMediator(ball, paddle1, paddle2)


def play_pong(winner=1):
    paddle1.position_paddle()
    paddle2.position_paddle()
    if winner == 2:
        ball.start(False)
    else:
        ball.start()

    while not mediator.has_ball_passed_paddles():
        ball.move()
        mediator.bounce()

    winner = mediator.who_won()
    scoreboard.update_score(score_player1=mediator.score_player_1, score_player2=mediator.score_player_2)
    ball.go_off_screen()
    play_pong(winner)


play_pong()

screen.exitonclick()

