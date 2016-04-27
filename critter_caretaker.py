#Финальная версия ухажера за зверюшкой
class Critter(object):
    def __init__(self,name,hunger=0,boredom=0):
        self.name=name
        self.hunger=hunger
        self.boredom=boredom
    def __pass_time(self):

        self.hunger+=1
        self.boredom+=1

    @property
    def mood(self):
        unhappiness = self.hunger +self.boredom
        if unhappiness <5:
            m = "Прекрасно"
        elif 5<=unhappiness<=10:
            m = "Неплохо"
        elif 11<= unhappiness <=15:
            m = "Не очень, знаешь."
        else:
            m = "Ужасно."
        return m
    def talk(self):
        print("Меня зовут",self.name,"и сейчас я чувствую себя",self.mood,"сейчас.\n")
        self.__pass_time()
    def eat(self,food=4):
        print("ВОТ Я ПОЕЛ И СИЛА ВЕРНУЛАСЬ КО МНЕ")
        self.hunger -=food
        if self.hunger<0:
            self.hunger=0
        self.__pass_time()
    def play(self,fun=4):
        print("Опять слил мид?")
        self.boredom -=fun
        if self.boredom <0:
            self.boredom=0
        self.__pass_time()
    @staticmethod
    def main():
        crit_name = input("Как вы назовете свое безобразное животное?")
        crit = Critter(crit_name)
        choise = None
        while choise !="0":
            print \
            ("""
            Моя зверюшка
             0 - Выйти
            1 - Узнать о самочувствии
            2 - Покормить
            3 - Поиграть
            """)
            choise = input("Ваш выбор: ")
            print()
            #exit
            if choise =="0":
                print("До свидания.")
            #talk with pet
            elif choise=="1":
                crit.talk()
            #feeding pet
            elif choise=="2":
                crit.eat()
            #play with pet
            elif choise=="3":
                crit.play()
            #error with input
            else:
                print("Извини, но такого пункта нет.",choise)
Critter.main()
