import model.animal as animal

class Dog (animal.Animal):
    def __init__(self, sound):
        super().set_sound(sound)