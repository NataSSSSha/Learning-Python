import tkinter
import game_model
import random
import game_state


class Game:
    def __init__(self):
        self.model = game_model.GameModel()
        self.state = game_state.GameState()
        self.tk = tkinter.Tk()
        self.tk.title('Lines')

        self.canvas = tkinter.Canvas(self.tk, width=self.model.grid_size * self.model.square_size,
                                height=self.model.grid_size * self.model.square_size)
        self.canvas.pack()

        self.tk.bind("<Button-1>", self.show_balls)

    def show_display(self):
        for i in range(self.model.grid_size):
            for j in range(self.model.grid_size):
                self.canvas.create_rectangle(i * self.model.square_size,
                                        j * self.model.square_size,
                                        i * self.model.square_size + self.model.square_size,
                                        j * self.model.square_size + self.model.square_size,
                                        fill='gray')

    def show_balls(self, event):
        if self.model.count_of_balls < self.model.max_count_of_balls:
            count = 0
            while count < 3:
                coordinates = self.state.add_balls()
                if self.model.matrix[coordinates[0]][coordinates[1]] == 0:
                    self.canvas.create_oval(coordinates[0] * self.model.square_size + self.model.oval_size,
                                            coordinates[1] * self.model.square_size + self.model.oval_size,
                                            coordinates[0] * self.model.square_size + self.model.square_size - self.model.oval_size,
                                            coordinates[1] * self.model.square_size + self.model.square_size - self.model.oval_size,
                                            fill=self.model.color_array[coordinates[2]])

                    self.state.change_matrix(coordinates[0], coordinates[1], 1)
                    count += 1
                    self.model.count_of_balls += 1

    def start_game(self):
        self.show_display()
        self.tk.mainloop()



