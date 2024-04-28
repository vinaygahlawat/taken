from source.card import Card

'''
Player object needs to represent either a human or computer player.
Needs to be able to accept a hand of Card objects dealt by the Dealer.
Needs to be able to select a card to play based on the board conditions.
This card needs to be removed from the hand and sent to the dealer.
'''
class Player:

    def __init__(self, dealer, id: str, is_computer: bool = True) -> None:
        self.is_computer = is_computer
        self.id = id
        self.hand = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        self._hand = value

    def play_card(self) -> Card:
        return self.choose_card()

    def choose_card(self) -> Card:
        card_to_play = self.hand[0]
        del(self.hand[0])
        return card_to_play
