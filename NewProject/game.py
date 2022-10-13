import tkinter
import game_model
import random


class Game:
    def __init__(self):
        self.model = game_model.GameModel()

        self.tk = tkinter.Tk()
        self.tk.title('Lines')

        self.canvas = tkinter.Canvas(self.tk, width=self.model.grid_size * self.model.square_size,
                                height=self.model.grid_size * self.model.square_size)
        self.canvas.pack()

    def show_display(self):
        for i in range(self.model.grid_size):
            for j in range(self.model.grid_size):
                self.canvas.create_rectangle(i * self.model.square_size,
                                        j * self.model.square_size,
                                        i * self.model.square_size + self.model.square_size,
                                        j * self.model.square_size + self.model.square_size,
                                        fill='gray')

    def add_balls(self):
        count = 0
        while count < 3:
            new_ball_coord_first = random.randint(0, self.model.grid_size - 1)
            new_ball_coord_second = random.randint(0, self.model.grid_size - 1)
            color_of_ball = random.randint(0, len(self.model.color_array) - 1)

            if self.model.matrix[new_ball_coord_first][new_ball_coord_second] == 0:
                self.canvas.create_oval(new_ball_coord_first * self.model.square_size + self.model.oval_size,
                                   new_ball_coord_second * self.model.square_size + self.model.oval_size,
                                   new_ball_coord_first * self.model.square_size + self.model.square_size - self.model.oval_size,
                                   new_ball_coord_second * self.model.square_size + self.model.square_size - self.model.oval_size,
                                   fill=self.model.color_array[color_of_ball])

                self.model.matrix[new_ball_coord_first][new_ball_coord_second] = 1
                count += 1

    def start_game(self):
        self.show_display()
        self.add_balls()

        self.tk.mainloop()



