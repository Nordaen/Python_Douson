# Демонстрация применения меток
from tkinter import *
root = Tk()
root.title("Это я, метка :3")
root.geometry("200x50")
# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()
# создание метки внутри рамки
lbl = Label(app, text ="Вот она я!")
lbl.grid()
# старт событийного окна
root.mainloop()

