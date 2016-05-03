# Сумашедший сказочник
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    # Создает элементы управления для генерации рассказа
    def create_widgets(self):
        # Метка с текстом - инструкцией
        Label(self,
              text = "Введите данные для создания нового рассказа"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        # Метка и поле ввода для имени персонажа
        Label(self,
              text = "Имя персонажа: ",
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)
        # Метка и поле ввода для существительного
        Label(self,
              text = "Существительное во мн.ч : "
              ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)
        # Метка и поле ввода для глагола
        Label(self,
              text = "Глагол в инфинитиве: "
              ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
        # Метка при группе флажков с прилагательными
        Label(self,
              text = "Прилагательное (-ые): "
              ).grid(row = 4, column = 0, sticky = W)
        # Флажок со словом "нетерпиливый"
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "Нетерпиливый",
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)
        # Флажок со словом "радостный"
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = "радостный",
                    variable = self.is_joyous
                    ).grid(row = 4, column = 2, sticky = W)
        # флажок со словом "Пронизывающий"
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "пронизывающий",
                    variable = self.is_electric
                    ).grid(row = 4, column = 3, sticky = W)
        # метка при переключатели с названиями частей тела
        Label(self,
              text = "Body Part: "
              ).grid(row = 5, column = 0, sticky = W)
        # переменная, содержащая название одной из частей тела
        self.body_part = StringVar()
        self.body_part.set(None)
        # переключатель с названиями частей тела
        body_parts = ["пупок", "большой палец ноги", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1
        # кнопка отсылки данных
        Button(self,
               text = "Получить рассказ",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)
        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def tell_story(self):
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "нетерпеливое, "
        if self.is_joyous.get():
            adjectives += "радостное, "
        if self.is_electric.get():
            adjectives += "пронизывающее, "
        body_part = self.body_part.get()
        # создание рассказа
        story = "Знаменитый путешественник"
        story += person
        story += "Уже совсем отчаялся довершить дело всей своей жизни - поиск города, в котором, по легенде обитали "
        story += noun.title()
        story += ", Но однажды "
        story += noun
        story += " и "
        story += person + " столкнулись лицом к лицу. "
        story += "Мощное, "
        story += adjectives
        story += " ни с чем не сравнимое чувство охватило душу путешественника. "
        story += " После стольких лет поисков цель была наконец достигнута. "
        story += person
        story += " ощутил, как на его " + body_part + " скатилась слезинка."
        story += "И тут внезапно "
        story += noun
        story += "перешли в атаку, и"
        story += person + " был ими многвенно сожран. "
        story += "Мораль? Если задумали "
        story += verb
        story += ", надо делать это с осторожностью. "
        # вывод рассказа на экран
        self.story_txt.delete("0.0", END)
        self.story_txt.insert("0.0", story)
root = Tk()
root.title("Сумашедший сказочник")
app = Application(root)
root.mainloop()


