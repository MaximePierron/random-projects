import time
import turtle
from highway import Highway
from player import Player
from car_manager import CarManager
from game_manager import GameManager
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.tracer(0)
screen.setup(600, 600)
scoreboard = Scoreboard()
highway = Highway()
car_manager = CarManager()


def play_the_game(sleep_time=0.05):
    player = Player()
    game_on = True
    while game_on:
        time.sleep(sleep_time)
        car_manager.add_to_car_pool()
        car_manager.move_all_cars()
        collision = GameManager.has_collided(player, car_manager.all_cars)
        if collision:
            game_on = False
        at_the_top = GameManager.has_reached_the_top(player, highway)
        if at_the_top:
            sleep_time -= 0.005
            scoreboard.level += 1
            scoreboard.update_level()
            player.hideturtle()
            play_the_game(sleep_time)
        screen.update()
    player.stop_moving()
    scoreboard.game_over()


play_the_game()

screen.exitonclick()
