# Демонстрация создания кнопок
from tkinter import *
# создание окна
root = Tk()
root.title("Бесполезные кнопки")
root.geometry("200x100")
# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()
# создание кнопки внутри рамки
bttn1 = Button(app,text ="Я ничего не делаю!")
bttn1.grid()
# другой способ создания - корректирование название после создания
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text ="И я тоже!")
# создание третьей кнопки внутри рамки
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "И я!"
# старт событийного цикла
root.mainloop()
