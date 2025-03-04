from hand import Hand

HAND_RANK_ORDER = {
    "Carte Haute": 0,
    "Paire": 1,
    "Deux Paires": 2,
    "Brelan": 3,
    "Quinte": 4,
    "Couleur": 5,
    "Full": 6,
    "Carré": 7,
    "Quinte Flush": 8,
    "Quinte Flush Royale": 9
}

def compare_hands(hand1, hand2):
    rank1 = HAND_RANK_ORDER[hand1.get_hand_rank()]
    rank2 = HAND_RANK_ORDER[hand2.get_hand_rank()]
    
    if rank1 > rank2:
        return "Main 1 gagne"
    elif rank2 > rank1:
        return "Main 2 gagne"
    
    # En cas d'égalité, comparer les cartes une par une
    for card1, card2 in zip(hand1.cards, hand2.cards):
        if card1.value > card2.value:
            return "Main 1 gagne"
        elif card1.value < card2.value:
            return "Main 2 gagne"
    
    return "Égalité"