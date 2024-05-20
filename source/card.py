class Card:
    
    def __init__(self, number, points) -> None:
        self.number: int = number
        self.points: int = points

    def sortFunc(e):
        return e.number

    def __str__(self) -> str:
        return str(f'{self.number}|{self.points}')
