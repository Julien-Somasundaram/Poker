from collections import Counter
from card import Card

class Hand:
    HAND_RANKS = [
        "Carte Haute", "Paire", "Deux Paires", "Brelan", "Quinte", "Couleur",
        "Full", "Carré", "Quinte Flush", "Quinte Flush Royale"
    ]

    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError("Une main doit contenir exactement 5 cartes.")
        self.cards = sorted(cards, key=lambda card: card.value, reverse=True)
        self.rank = self.evaluate_hand()

    def evaluate_hand(self):
        values = [card.value for card in self.cards]
        suits = [card.suit for card in self.cards]
        value_counts = Counter(values)
        sorted_values = sorted(values, reverse=True)
        unique_values = list(value_counts.keys())
        
        is_flush = len(set(suits)) == 1
        is_straight = len(unique_values) == 5 and (max(unique_values) - min(unique_values) == 4)
        is_royal = is_flush and is_straight and max(values) == 14
        
        if is_royal:
            return "Quinte Flush Royale"
        if is_flush and is_straight:
            return "Quinte Flush"
        if 4 in value_counts.values():
            return "Carré"
        if 3 in value_counts.values() and 2 in value_counts.values():
            return "Full"
        if is_flush:
            return "Couleur"
        if is_straight:
            return "Quinte"
        if 3 in value_counts.values():
            return "Brelan"
        if list(value_counts.values()).count(2) == 2:
            return "Deux Paires"
        if 2 in value_counts.values():
            return "Paire"
        return "Carte Haute"

    def get_hand_rank(self):
        return self.rank

    def __repr__(self):
        return f"Main: {', '.join(map(str, self.cards))} ({self.rank})"