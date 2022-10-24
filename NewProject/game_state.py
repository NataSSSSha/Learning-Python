import game_model
import random

class GameState:
    def new_game(self):
        for i in range(game_model.GameModel.grid_size):
            for j in range(game_model.GameModel.grid_size):
                game_model.GameModel.matrix[i][j] = ''

    def add_balls(self):
        count = 0
        if game_model.GameModel.count_of_balls < game_model.GameModel.max_count_of_balls:
            while count < 3:
                new_ball_coord_first = random.randint(0, game_model.GRID_SIZE - 1)
                new_ball_coord_second = random.randint(0, game_model.GRID_SIZE - 1)
                color_of_ball = random.randint(0, len(game_model.GameModel.color_array) - 1)

                if game_model.GameModel.matrix[new_ball_coord_first][new_ball_coord_second] == '':
                    self.change_matrix(new_ball_coord_first, new_ball_coord_second, game_model.GameModel.color_array[color_of_ball])
                    count += 1
                    game_model.GameModel.count_of_balls += 1

    def change_matrix(self, first_coord, second_coord, value):
        game_model.GameModel.matrix[first_coord][second_coord] = value
