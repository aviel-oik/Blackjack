import random

def build_standard_deck() -> list[dict]:
    lst = []
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suite = ["H", "C", "D", "S"]
    for s in suite:
        for r in rank:
            card = {"rank": r, "suit": s}
            lst.append(card)
    return lst




def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range(0, swaps):
        i = random.randint(0, len(deck) - 1)
        card_1 = deck[i]
        valid_card = False
        while not valid_card:
            j = random.randint(0, len(deck) - 1)
            valid_card = True
            if i == j:
                valid_card = False
            if card_1["suit"] == "H" and j%5 != 0:
                valid_card = False
            if card_1["suit"] == "C" and j%3 != 0:
                valid_card = False
            if card_1["suit"] == "D" and j%2 != 0:
                valid_card = False
            if card_1["suit"] == "S" and j%7 != 0:
                valid_card = False
        tmp = deck[i]
        deck[i] = deck[j]
        deck[j] = tmp
    return deck











