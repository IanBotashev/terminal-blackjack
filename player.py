import copy
from hand import MAX_HAND_VALUE, Hand
from card import Face, Card, Suit


class Player:
    def __init__(self, hand, game):
        self.hand = hand
        self.game = game
        self.staying = False

    def hit(self):
        """Hits this player."""
        if self.staying:
            return

        self.game.add_card_to_hand(self.hand)

    def stay(self):
        """Makes this player stay. Cannot 'unstay'"""
        self.staying = True

    def next_move(self):
        """For AI players, decides what they should do."""
        if self.staying:
            return
        if self.chance_to_lose() < 0.6:
            print("dealer hit.")
            self.hit()
        else:
            print("dealer staying.")
            self.stay()

    def chance_to_lose(self):
        """Calculates the chance that a hit might end up with a losing hand."""
        losing_cards = 0
        for face in [b.value for b in Face]:
            imaginary_hand = Hand(self.hand.cards.copy())
            imaginary_hand.cards.append(Card(Suit.CLUBS, Face(face), False))

            if imaginary_hand.get_hand_value() > MAX_HAND_VALUE:
                losing_cards += 1

        return losing_cards / len([b.value for b in Face])
