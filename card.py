from enum import Enum
from dataclasses import dataclass


class Suit(Enum):
    DIAMONDS = 0
    CLUBS = 1
    SPADES = 2
    HEARTS = 3


class Face(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 11
    KING = 12
    ACE = 13


values = {
    Face.TWO: 2,
    Face.THREE: 3,
    Face.FOUR: 4,
    Face.FIVE: 5,
    Face.SIX: 6,
    Face.SEVEN: 7,
    Face.EIGHT: 8,
    Face.NINE: 9,
    Face.TEN: 10,
    Face.JACK: 10,
    Face.QUEEN: 10,
    Face.KING: 10,
    Face.ACE: [1, 11],
}


@dataclass
class Card:
    """Representation of a card with a suit and face."""
    suit: Suit
    face: Face
    hidden: bool

    def get_value(self):
        """Gets the value of this cards value."""
        return values[self.face]

    def __repr__(self):
        """Returns a stylized string for this card. Prints 'hidden' if it's a hidden one."""
        if self.hidden:
            return "(hidden card)"

        return f"{self.face.name} of {self.suit.name}"
