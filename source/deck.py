from source.card import Card

class Deck:

    # Static class attributes
    CardDeck = []

    def __init__(self, size, point_values) -> None:

        for i in range (1, size+1):
            card = Card(i, point_values.get(i,1))
            Deck.CardDeck.append(card)
