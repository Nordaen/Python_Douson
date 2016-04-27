class Critter(object):
    def __init__(self,name):
        print("Появилась на свет новая зверюга!")
        self.__name = name
    @property
    def name(self):
        return self.__name
