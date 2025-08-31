from overrides import overrides
from bonus_task.animal import Animal
from bonus_task.pet import Pet

class Cat(Animal, Pet):
    def __init__(self, legs, name: str):
        super().__init__(legs, name)
        self.name = name

    @overrides
    def get_name(self) -> str:
        return self.name

    @overrides
    def set_name(self, name: str):
        self.name = name

    @overrides
    def play(self):
        print(f"{self.name} is playing")

    @overrides
    def eat(self):
        print("Cat eats")