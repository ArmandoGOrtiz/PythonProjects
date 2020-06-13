from random import shuffle
from card import Card


class Deck:

    # Initialize deck to contain cards
    # numbered 2 to 14.
    def __init__(self):
        self._cards = []
        for suit in ['C', 'D', 'H', 'S']:
            for rank in range(2, 15):
                c = Card(rank, suit)
                self._cards.append(c)
                c = self._cards.pop()
                self._cards.insert(0, c)
    # Display deck as a str object.

    def __str__(self):
        output = ""
        for card in self._cards:
            output += " " + str(card)
        return output

    # Remove top card from the deck
    # and return it.
    def deal(self):
        return self._cards.pop()

    # Add a card to top of deck
    def add_to_top(self, the_card):
        self._cards.append(the_card)

    # Add a card to bottom of deck
    def add_to_bottom(self, the_card):
        self._cards.insert(0, the_card)

    # Return number of cards in deck
    def count(self):
        return len(self._cards)

    # Return True if deck is empty,
    # False, otherwise.
    def is_empty(self):
        return len(self._cards) == 0

    # Shuffle the cards
    def shuffle(self):
        shuffle(self._cards)
