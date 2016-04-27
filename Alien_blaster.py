#Демонстрация взаимодействия объектов
class Player(object):
    def blast(self,enemy):
        print("Игрок стреляет во врага","\n")
        enemy.die()
class Alien(object):
    def die(self):
        print("Alien has been slain.")
print("\t\tГибель пришельца\n")
hero=Player()
invader=Alien()
hero.blast(invader)