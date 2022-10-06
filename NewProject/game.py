import tkinter
import game_model


class Game:
    def __init__(self):
        self.model = game_model.GameModel()

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
                canvas.create_oval(i * self.model.square_size + self.model.oval_size,
                                   j * self.model.square_size + self.model.oval_size,
                                   i * self.model.square_size + self.model.square_size - self.model.oval_size,
                                   j * self.model.square_size + self.model.square_size - self.model.oval_size,
                                   fill=self.model.color_array[i])

        tk.mainloop()