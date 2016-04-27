class Critter(object):
    total=0
    @staticmethod
    def status():
        print("Всего зверюшек сейчас:",Critter.total)
    def __init__(self,name):
        print("Появилась на свет новая зверюшка!")
        self.name=name
        Critter.total+=1
    def __str__(self):
        rep  = "Объект класса Critter \n"
        rep +="имя: " + self.name +"\n"
        return rep
    def talk(self):
        print("Привет. Меня зовут",self.name,"\n")
crit1=Critter("Бобик")
crit1.talk()
crit2=Critter("Барбос")
crit2.talk()
crit3=Critter("Василий")
crit3.talk()
print("выводим crit1 на экран")
print(crit2)
print("Доступ к crit1.name")
print(crit2.name)
Critter.status()
