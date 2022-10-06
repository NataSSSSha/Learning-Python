import dataclasses


@dataclasses.dataclass
class GameModel:
    grid_size = 6
    square_size = 100
    oval_size = 20
    color_array = ['red', 'green', 'yellow', 'white', 'blue', 'pink']