class Animal:
    __instance = None

    # def __init__(self, sound):
    #     self.__sound = sound

    def make_sound(self):
        print (self.__sound)

    def get_sound(self):
        return self.__sound

    def set_sound(self, sound):
        self.__sound = sound

    @staticmethod
    def instance():
        if not Animal.__instance:
            Animal.__instance = Animal()
        return Animal.__instance


#singleton = Animal("")