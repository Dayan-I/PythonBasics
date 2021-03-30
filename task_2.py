from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, v=None, h=None):
        self.v = v
        self.h = h

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Suit(Clothes):
    @property
    def tissue_consumption(self):
        return (2 * self.h + 0.3) / 100


class Coat(Clothes):
    @property
    def tissue_consumption(self):
        return self.v / 6.5 + 0.5



