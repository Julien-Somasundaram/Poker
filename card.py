class Card:
    RANKS = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
             "Valet": 11, "Dame": 12, "Roi": 13, "As": 14}
    SUITS = {"Coeur", "Carreau", "Trèfle", "Pique"}

    def __init__(self, rank, suit):
        if rank not in self.RANKS or suit not in self.SUITS:
            raise ValueError("Carte invalide")
        self.rank = rank
        self.suit = suit
        self.value = self.RANKS[rank]

    def __repr__(self):
        return f"{self.rank} de {self.suit}"
    
    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value
