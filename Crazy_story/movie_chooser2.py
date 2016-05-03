# Демонстрирует переключатель
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Укажите ваш любимый жанр кино"
              ).grid(row = 0, column = 0, sticky = W)
# Переменная для хранения сведений о единственном любимом жанре.
        self.favourite = StringVar()
        self.favourite.set(None)
        # Положения "Комедия" переключателя
        Radiobutton(self,
                    text = "Комедия",
                    variable = self.favourite,
                    value = "комедия.",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)
        # Положение "Драма" переключателя
        Radiobutton(self,
                    text = "Драма",
                    variable = self.favourite,
                    value = "драма",
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)
        # Положение "Кино о любви
        Radiobutton(self,
                    text = "Любовные",
                    variable = self.favourite,
                    value = "любовные",
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)
        # Текстовая область с результатами
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
    def update_text(self):
        message = "Ваш любимый жанр кино: "
        message +=self.favourite.get()
        self.results_txt.delete("0.0", END)
        self.results_txt.insert("0.0", message)
root = Tk()
root.title("Киноман - 2")
app = Application(root)
root.mainloop()