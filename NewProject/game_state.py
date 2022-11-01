import game_model
import random
import ball_coordinates

class GameState:
    # рисует пустое поле без шаров, очищает матрицу
    def new_game(self):
        for i in range(game_model.GameModel.grid_size):
            for j in range(game_model.GameModel.grid_size):
                game_model.GameModel.matrix[i][j] = ''

    #добавляет в матрицу 3 новых шара (старым способом)
    def add_balls(self):
        count = 0
        array_of_balls = []
        if game_model.GameModel.count_of_balls < game_model.GameModel.max_count_of_balls:
            for i in range(game_model.GameModel.grid_size):
                for j in range(game_model.GameModel.grid_size):
                    if game_model.GameModel.matrix[i][j] == '':
                        new_ball = ball_coordinates.BallCoordinates(i, j)
                        array_of_balls.append(new_ball)
            coords = random.choices(array_of_balls, k=3)
            while count < 3:
                color_of_ball = random.randint(0, len(game_model.GameModel.color_array) - 1)
                self.change_matrix(coords[count].first_coordinate, coords[count].second_coordinate, game_model.GameModel.color_array[color_of_ball])
                count += 1
                game_model.GameModel.count_of_balls += 1

    #изменяет матрицу с шарами (принимает координаты шара и его цвет)
    def change_matrix(self, first_coord, second_coord, value):
        game_model.GameModel.matrix[first_coord][second_coord] = value
