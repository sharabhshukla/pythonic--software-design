from enum import Enum, auto
import os

class Suite(Enum):
    DIAMOND = auto()
    CLUB = auto()
    HEART = auto()
    SPADE = auto()

class Value(Enum):
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()

class Card:
    def __init__(self, suite: Suite, value: Value):
        self.suite = suite
        self.value = value

    @property
    def suite(self):
        return self._suite

    @property
    def value(self):
        return self._value

    @suite.setter
    def suite(self, suite: Suite):
        if suite not in Suite:
            raise Exception
        self._suite = suite

    @value.setter
    def value(self, value: Value):
        if value not in Value:
            raise Exception
        self._value = value

    def __repr__(self):
        return 'Card {} of {}'.format(self.value, self.suite)

class Deck:
    def __init__(self):
        self.cards = [Card(s,v) for s in Suite for v in Value]


def main():
    card1 = Card(Suite.DIAMOND, Value.TWO)
    print(card1)
    deck1 = Deck()
    print(deck1.cards)

if __name__ == '__main__':
    main()
    print(os.environ.get('TESTSTR'))