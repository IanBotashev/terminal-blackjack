from dataclasses import dataclass
from card import Card, Suit, Face

MAX_HAND_VALUE = 21


@dataclass
class Hand:
    cards: list[Card]

    def show_cards(self):
        """Unhides all the cards in this hand."""
        for card in self.cards:
            card.hidden = False

    def get_hand_value(self):
        """Gets the value of this hand."""
        result = 0
        multiple_value_cards = []
        for card in self.cards:
            value = card.get_value()
            # If this hand has only one possible value, just add it in.
            if type(value) == int:
                result += value
                continue
            multiple_value_cards.append(value)

        # Check multiple values AFTER adding everything up, so we can properly decide which values to use.
        for multiple_value_card in multiple_value_cards:
            value_to_add = min(multiple_value_card)
            # Get the maximum value that we can add without going over the max hand value.
            for possible_value in multiple_value_card:
                if result + possible_value <= MAX_HAND_VALUE:
                    value_to_add = possible_value

            result += value_to_add

        return result
