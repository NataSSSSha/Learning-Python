import game_model
import random


class BallCoordinates:
    first_coordinate = 0
    second_coordinate = 0
    array_of_balls = {}

    def __init__(self, first, second):
        self.first_coordinate = first
        self.second_coordinate = second

