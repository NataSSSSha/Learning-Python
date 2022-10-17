import dataclasses

GRID_SIZE = 6


@dataclasses.dataclass
class GameModel:
    grid_size = GRID_SIZE
    square_size = 100
    oval_size = 20
    color_array = ['red', 'green', 'yellow', 'white', 'blue', 'pink']
    matrix = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
    count_of_balls = 0
    max_count_of_balls = grid_size * grid_size - 2
