import game_model
import random


class GameState:

    def add_balls(self):
        new_ball_coord_first = random.randint(0, game_model.GRID_SIZE - 1)
        new_ball_coord_second = random.randint(0, game_model.GRID_SIZE - 1)
        color_of_ball = random.randint(0, len(game_model.GameModel.color_array) - 1)

        coordinates = [new_ball_coord_first, new_ball_coord_second, color_of_ball]

        return coordinates

    def change_matrix(self, first_coord, second_coord, value):
        game_model.GameModel.matrix[first_coord][second_coord] = value
