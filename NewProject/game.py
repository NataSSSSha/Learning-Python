import tkinter
import game_model
import game_state

class Game:
    def __init__(self):
        self.model = game_model.GameModel()
        self.state = game_state.GameState()
        self.state.new_game()
        self.tk = tkinter.Tk()
        self.tk.title('Lines')

        self.canvas = tkinter.Canvas(self.tk, width=self.model.grid_size * self.model.square_size,
                                height=self.model.grid_size * self.model.square_size)
        self.canvas.pack()

        self.tk.bind("<Button-1>", self.on_click)

    #рисует поле с квадратами(ячейками)
    def draw_board(self):
        for i in range(self.model.grid_size):
            for j in range(self.model.grid_size):
                self.canvas.create_rectangle(i * self.model.square_size,
                                        j * self.model.square_size,
                                        i * self.model.square_size + self.model.square_size,
                                        j * self.model.square_size + self.model.square_size,
                                        fill='gray')
    # рисует матрицу с шарами
    def draw_balls(self):
        for i in range(self.model.grid_size):
            for j in range(self.model.grid_size):
                if self.model.matrix[i][j] != '':
                    self.canvas.create_oval(i * self.model.square_size + self.model.oval_size,
                                            j * self.model.square_size + self.model.oval_size,
                                            i * self.model.square_size + self.model.square_size - self.model.oval_size,
                                            j * self.model.square_size + self.model.square_size - self.model.oval_size,
                                            fill=self.model.matrix[i][j])
    # выводит текущее состояние
    def draw_state(self):
        self.draw_balls()

    # действие при клике (добавление шаров в матрицу, и отображение матрицы)
    def on_click(self, event):
        self.state.add_balls()
        self.draw_state()

    # действие при начале игры (игровое поле)
    def start_game(self):
        self.draw_board()
        self.tk.mainloop()



