# Демонстрация создания класса в оконном приложении на основе tkinter
from tkinter import *

class Application(Frame):
    """GUI - приложение с тремя кнопками."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text = "Я ничего не делаю!")
        self.button1.grid()
        self.button2 = Button(self, text = "И я тоже!")
        self.button2.grid()
        self.button3 = Button(self, text = "И я!")
        self.button3.grid()
# Основная часть
root = Tk()
root.title("Бесполезные кнопки - 2")
root.geometry("200x85")
app = Application(root)
root.mainloop()
