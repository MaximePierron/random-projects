from ball import Ball
from paddle import Paddle
from random import randint


class PongMediator(object):
    def __init__(self, ball, paddle1, paddle2):
        if ball is None:
            self.ball = Ball()
        else:
            self.ball = ball

        if paddle1 is None:
            self.paddle1 = Paddle("Up", "Down", 350)
        else:
            self.paddle1 = paddle1

        if paddle2 is None:
            self.paddle2 = Paddle("w", "s", -350)
        else:
            self.paddle2 = paddle2

        self.score_player_1 = 0
        self.score_player_2 = 0

    def has_ball_passed_paddles(self):
        if self.ball.xcor() < self.paddle2.starting_x_cor or self.ball.xcor() > self.paddle1.starting_x_cor:
            return True
        return False

    def is_within_paddle_height(self, paddle):
        return paddle.ycor() - 50 <= self.ball.ycor() <= paddle.ycor() + 50

    i = 0
    j = 0

    def bounce(self):
        if self.ball.xcor() <= self.paddle2.xcor() + 20 and self.is_within_paddle_height(self.paddle2):
            self.i += 1
            if not self.ball.sleep_time - 0.0001 <= 0:
                self.ball.sleep_time -= 0.001
            if 180 <= self.ball.heading() <= 270:
                if self.i % 2 == 0:
                    self.ball.setheading(315 + randint(0, 5))
                else:
                    self.ball.setheading(315 - randint(0, 5))
            else:
                if self.i % 2 == 0:
                    self.ball.setheading(45 + randint(0, 5))
                else:
                    self.ball.setheading(45 - randint(0, 5))
        elif self.ball.xcor() >= self.paddle1.xcor() - 20 and self.is_within_paddle_height(self.paddle1):
            self.j += 1
            self.ball.sleep_time -= 0.01
            if 0 <= self.ball.heading() <= 90:
                if self.j % 2 == 0:
                    self.ball.setheading(135 + randint(0, 5))
                else:
                    self.ball.setheading(135 - randint(0, 5))
            else:
                if self.j % 2 == 0:
                    self.ball.setheading(225 + randint(0, 5))
                else:
                    self.ball.setheading(225 - randint(0, 5))

    def who_won(self):
        if self.ball.xcor() < self.paddle2.starting_x_cor:
            self.score_player_2 += 1
            return 1
        elif self.ball.xcor() > self.paddle1.starting_x_cor:
            self.score_player_1 += 1
            return 2
        else:
            return 3
