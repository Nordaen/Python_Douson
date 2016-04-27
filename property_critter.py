class Critter(object):
    def __init__(self,name):
        print("Появилась на свет новая зверюга!")
        self.__name = name
    @property
    def name(self):
        return self.__name
   @name.setter
    def name(self,new_name):
        if new_name=="":
            print("Имя зверюшки не может быть пустой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")
    def talk(self):
        print("Привет, меня зовут",self.name)
crit = Critter("Барбос")
crit.talk()
print("\nМоего зверя зовут",end=" ")
print(crit.name)
print("\nПробую изменить имя на Горо")
crit.name = "Горо"
print("\nМоего зверя зовут",end=" ")
print(crit.name)
    
