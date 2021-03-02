import model.animal as animal

class Cat (animal.Animal):
    def __init__(self, sound):
        super().set_sound(sound)