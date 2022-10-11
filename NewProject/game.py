import tkinter
import game_model
import random


class Game:
    def __init__(self):
        self.model = game_model.GameModel()

    matrix = [[0 for x in range(6)] for y in range(6)]

    def show_display(self):
        tk = tkinter.Tk()
        tk.title('Lines')

        canvas = tkinter.Canvas(tk, width=self.model.grid_size * self.model.square_size,
                                height=self.model.grid_size * self.model.square_size)
        canvas.pack()

        for i in range(self.model.grid_size):
            for j in range(self.model.grid_size):
                canvas.create_rectangle(i * self.model.square_size,
                                        j * self.model.square_size,
                                        i * self.model.square_size + self.model.square_size,
                                        j * self.model.square_size + self.model.square_size,
                                        fill='gray')

        count = 0
        while count < 3:
            new_ball_coord_first = random.randint(0, self.model.grid_size - 1)
            new_ball_coord_second = random.randint(0, self.model.grid_size - 1)
            if self.matrix[new_ball_coord_first][new_ball_coord_second] == 0:
                canvas.create_oval(new_ball_coord_first * self.model.square_size + self.model.oval_size,
                                   new_ball_coord_second * self.model.square_size + self.model.oval_size,
                                   new_ball_coord_first * self.model.square_size + self.model.square_size - self.model.oval_size,
                                   new_ball_coord_second * self.model.square_size + self.model.square_size - self.model.oval_size,
                                   fill=self.model.color_array[new_ball_coord_first])
                self.matrix[new_ball_coord_first][new_ball_coord_second] = 1
                count += 1

        tk.mainloop()
