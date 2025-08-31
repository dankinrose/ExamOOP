from abc import ABC, abstractmethod

class Pet(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_name(self, name: str):
        pass

    @abstractmethod
    def play(self):
        pass