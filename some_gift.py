from overrides import overrides
from surprisable import Surprisable

class SomeGift(Surprisable):

    @overrides
    def open_gift(self):
        print(f"Congratulations! you got a new gift! Enjoy!")
