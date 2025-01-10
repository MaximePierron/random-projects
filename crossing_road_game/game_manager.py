class GameManager:
    @staticmethod
    def has_collided(player, all_cars):
        for car in all_cars:
            if car.ycor() == player.ycor() and car.xcor() - 10 <= player.xcor() <= car.xcor() + 10:
                return True
        return False

    @staticmethod
    def has_reached_the_top(player, highway):
        if player.ycor() > highway.STARTING_Y + highway.number_of_lane*30:
            return True
        return False
