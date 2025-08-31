from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, legs: int):
        self.legs = legs

    def walk(self):
        print(f"Walking on {self.legs} legs")

    @abstractmethod
    def eat(self):
        pass