class Critter(object):
    def __init__(self,name,mood):
        print("Появилась на свет зверюга")
        self.name = name #open attribute
        self.__mood = mood #closed attibute
    def talk(self):
        print("\nМеня зовут:",self.name)
        print("Сейчас я чувствую себя:",self.__mood,"\n")
    def __private_method(self):
        print("я закрытый")
    def public_method(self):
        print("А я открытый, лол))00")
        self.__private_method()
crit = Critter(name="Василий", mood="неочень")
crit.talk()
crit.public_method()
