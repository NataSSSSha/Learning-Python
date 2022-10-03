from tkinter import Canvas, Tk


def show_display():
    tk = Tk()
    tk.title('Lines')

    greed_size = 6
    square_size = 100

    canvas = Canvas(tk, width=greed_size*square_size, height=greed_size*square_size)
    canvas.pack()

    for i in range(greed_size):
        for j in range(greed_size):
            canvas.create_rectangle(i * square_size, j * square_size,
                                    i * square_size + square_size,
                                    j * square_size + square_size, fill='gray')

    tk.mainloop()


show_display()






