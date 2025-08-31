from bonus_task.animal import Animal
from overrides import overrides

class Spider(Animal):
    def __init__(self, legs):
        super().__init__(legs)

    @overrides
    def eat(self):
        print("Spider eats")