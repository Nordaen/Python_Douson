class Critter(object):
    def __init__(self,name):
        print("Появилась на свет новая хрень!")
        self.__name = name
    @property
    def name(self):
        return self.__name