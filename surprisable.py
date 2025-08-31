from abc import ABC, abstractmethod


class Surprisable(ABC):

    @abstractmethod
    def open_gift(self):
        pass

