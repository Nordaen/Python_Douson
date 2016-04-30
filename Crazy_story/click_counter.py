# Демонстрация связывания событий с обработчиками
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 # кол-во нажатий
        self.create_widget()

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn["text"] = "Количество щелчков: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
    def update_count(self):
        self.bttn_clicks +=1
        self.bttn["text"] = "Количество щелчков: " + str(self.bttn_clicks)
# Основная часть
root = Tk()
root.title("Количество щелчков")
root.geometry("200x50")
app = Application(root)
root.mainloop()
