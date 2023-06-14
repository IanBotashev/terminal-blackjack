from hand import Hand, MAX_HAND_VALUE
from card import Face, Suit, Card
import random
from player import Player


class AvailableCards:
    def __init__(self):
        self.available_cards = self.generate_cards()

    def pull_random(self, hidden=False):
        """Pulls a random card from available cards, then removes it from the available list."""
        try:
            random_card = random.choice(self.available_cards)
        except IndexError:
            print("All cards exhausted.")
            exit()

        self.available_cards.remove(random_card)
        random_card.hidden = hidden
        return random_card

    @staticmethod
    def generate_cards():
        """Generates all possible cards."""
        result = []
        for suit in [a.value for a in Suit]:
            for face in [b.value for b in Face]:
                result.append(Card(Suit(suit), Face(face), False))

        return result


class Game:
    def __init__(self):
        self.available_cards = AvailableCards()
        self.human = Player(self.generate_hand(False), self)
        self.dealer = Player(self.generate_hand(True), self)

    def add_card_to_hand(self, hand):
        """Adds a card from the available cards to a passed-in hand."""
        hand.cards.append(self.available_cards.pull_random())

    def generate_hand(self, hide_cards):
        """Generates a hand with two random cards."""
        cards = []
        for i in range(2):
            # If we have to hide cards, hide it only if it's the first.
            cards.append(self.available_cards.pull_random(i == 0 and hide_cards))
        return Hand(cards)

    def run(self):
        # While neither are staying, play.
        while not self.human.staying or not self.dealer.staying:
            self.player_handler()
            self.dealer.next_move()

        final_hand_string = f"Your final hand: {self.human.hand.cards}"
        print("=" * len(final_hand_string))
        print(final_hand_string)
        self.dealer.hand.show_cards()
        print(f"Dealer's final hand: {self.dealer.hand.cards}")
        print(f"Your final value: {self.human.hand.get_hand_value()}")
        print(f"Dealer's final value: {self.dealer.hand.get_hand_value()}")
        self.announce_winner()
        print("=" * len(final_hand_string))

    def player_handler(self):
        """Handles player input."""

        # If the human is staying, do nothing.
        if self.human.staying:
            return

        print(f"You: {self.human.hand.cards}")
        print(f"Dealer: {self.dealer.hand.cards}")

        # Lowercase the users input.
        while True:
            action = input("Hit or Stay? ").lower()
            if action == "hit" or action == "h":
                self.human.hit()
                break
            elif action == "stay" or action == "s":
                self.human.stay()
                print("Staying. Waiting for dealer.")
                break
            else:
                print("unknown command.")

    def announce_winner(self):
        """Prints in the console who won."""
        player_value = self.human.hand.get_hand_value()
        dealer_value = self.dealer.hand.get_hand_value()

        if (player_value == MAX_HAND_VALUE and len(self.human.hand.cards) == 2) or (dealer_value == MAX_HAND_VALUE and len(self.dealer.hand.cards) == 2):
            print("Blackjack.")

        print("---", end="")
        if (dealer_value < player_value <= MAX_HAND_VALUE) or (dealer_value > MAX_HAND_VALUE >= player_value):
            print("You win.")
        elif (player_value <= dealer_value <= MAX_HAND_VALUE) or (dealer_value <= MAX_HAND_VALUE < player_value):
            print("Dealer wins.")
        else:
            print("No one wins.")

    @staticmethod
    def generate_cards():
        """Generates all possible cards."""
        result = []
        for suit in [a.value for a in Suit]:
            for face in [b.value for b in Face]:
                result.append(Card(Suit(suit), Face(face), False))

        return result
