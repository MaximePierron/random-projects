from random import randint

from car import Car
import queue


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.last_five_lanes = queue.Queue()

    def add_to_car_pool(self):
        random_chance = randint(1, 6)
        if random_chance == 6 or random_chance == 4:
            car = Car()
            lane_number = car.set_lane()
            while lane_number in self.last_five_lanes.queue:
                lane_number = car.set_lane()
            self.last_five_lanes.put(lane_number)
            if self.last_five_lanes.qsize() > 5:
                self.last_five_lanes.get()
            car.go_to_lane(lane_number)
            self.all_cars.append(car)

    def move_all_cars(self):
        for car in self.all_cars:
            car.move()
