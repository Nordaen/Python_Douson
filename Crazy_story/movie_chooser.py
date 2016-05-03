# Демонстрация применения флажков
# ДОБАВЛЕНО: добавил функционал - когда ничего не выбрано. Исправил баги: в книге не указаны названия Checkbutton'ов.
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "Укажите ваши любимые жанры кино").grid(row = 0, column = 0, sticky = W)
        Label(self, text = "Выберите то, что вам по вкусу:").grid(row = 1, column = 0, sticky = W)
    # Создание метки "Комедия". Интересно - элемент не связан с какой-либо переменной - статус получим из likes_comedy
        self.likes_comedy = BooleanVar()
        Checkbutton(self, text = "Комедия", variable = self.likes_comedy, command = self.update_text).grid(row = 2, column = 0, sticky = W)
        # Создание метки "Драма"
        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text = "Драма", # ДОБАВЛЕНО
                    variable = self.likes_drama,
                    command = self.update_text
                    ).grid(row = 3, column =0, sticky = W)
        # Фладок "Фильм о любви"
        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text = "Романтика", # ДОБАВЛЕНО
                    variable = self.likes_romance,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column =0, columnspan = 3)

    def update_text(self):
        likes = ""
        if self.likes_comedy.get():
            likes += "Вам нравятся комедии.\n"
        if self.likes_drama.get():
            likes += "Вам нравятся драмы.\n"
        if self.likes_romance.get():
            likes += "Вам нравятся любовные темы.\n"
        if likes =="":
            likes += "Вам ничего не нравится. Жаль." # ДОБАВЛЕНО
        self.results_txt.delete("0.0", END) # ДОБАВЛЕНО
        self.results_txt.insert("0.0", likes) # ДОБАВЛЕНО
root = Tk()
root.title("Киноман")
app = Application(root)
root.mainloop()


