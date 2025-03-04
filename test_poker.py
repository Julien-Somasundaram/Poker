import unittest
from card import Card
from hand import Hand
from poker import compare_hands

class TestPoker(unittest.TestCase):
    def test_card_creation(self):
        card = Card("As", "Coeur")
        self.assertEqual(card.rank, "As")
        self.assertEqual(card.suit, "Coeur")

    def test_hand_creation(self):
        cards = [
            Card("As", "Coeur"), Card("Roi", "Coeur"), Card("Dame", "Coeur"),
            Card("Valet", "Coeur"), Card("10", "Coeur")
        ]
        hand = Hand(cards)
        self.assertEqual(len(hand.cards), 5)

    def test_royal_flush(self):
        cards = [
            Card("As", "Coeur"), Card("Roi", "Coeur"), Card("Dame", "Coeur"),
            Card("Valet", "Coeur"), Card("10", "Coeur")
        ]
        hand = Hand(cards)
        self.assertEqual(hand.get_hand_rank(), "Quinte Flush Royale")
    
    def test_straight_flush(self):
        cards = [
            Card("9", "Pique"), Card("8", "Pique"), Card("7", "Pique"),
            Card("6", "Pique"), Card("5", "Pique")
        ]
        hand = Hand(cards)
        self.assertEqual(hand.get_hand_rank(), "Quinte Flush")
    
    def test_four_of_a_kind(self):
        cards = [
            Card("7", "Coeur"), Card("7", "Carreau"), Card("7", "Pique"),
            Card("7", "Trèfle"), Card("9", "Coeur")
        ]
        hand = Hand(cards)
        self.assertEqual(hand.get_hand_rank(), "Carré")
    
    def test_full_house(self):
        cards = [
            Card("10", "Coeur"), Card("10", "Carreau"), Card("10", "Pique"),
            Card("4", "Trèfle"), Card("4", "Coeur")
        ]
        hand = Hand(cards)
        self.assertEqual(hand.get_hand_rank(), "Full")

    def test_flush(self):
        cards = [
            Card("As", "Trèfle"), Card("10", "Trèfle"), Card("7", "Trèfle"),
            Card("6", "Trèfle"), Card("2", "Trèfle")
        ]
        hand = Hand(cards)
        self.assertEqual(hand.get_hand_rank(), "Couleur")
    
    def test_straight(self):
        cards = [
            Card("9", "Coeur"), Card("8", "Carreau"), Card("7", "Pique"),
            Card("6", "Trèfle"), Card("5", "Coeur")
        ]
        hand = Hand(cards)
        self.assertEqual(hand.get_hand_rank(), "Quinte")
    
    def test_compare_hands(self):
        hand1 = Hand([
            Card("As", "Coeur"), Card("Roi", "Coeur"), Card("Dame", "Coeur"),
            Card("Valet", "Coeur"), Card("10", "Coeur")
        ])
        hand2 = Hand([
            Card("9", "Pique"), Card("8", "Pique"), Card("7", "Pique"),
            Card("6", "Pique"), Card("5", "Pique")
        ])
        result = compare_hands(hand1, hand2)
        self.assertEqual(result, "Main 1 gagne")

    def test_tie_hands(self):
        hand1 = Hand([
            Card("Roi", "Trèfle"), Card("Roi", "Coeur"), Card("Roi", "Carreau"),
            Card("5", "Pique"), Card("5", "Coeur")
        ])
        hand2 = Hand([
            Card("Roi", "Carreau"), Card("Roi", "Trèfle"), Card("Roi", "Pique"),
            Card("5", "Trèfle"), Card("5", "Carreau")
        ])
        result = compare_hands(hand1, hand2)
        self.assertEqual(result, "Égalité")

if __name__ == "__main__":
    unittest.main()
