from source.card import Card

class Deck:

    def __init__(self, size, point_values) -> None:
        self.card_deck = []

        for i in range (1, size+1):
            card = Card(i, point_values.get(i,1))
            self.card_deck.append(card)
