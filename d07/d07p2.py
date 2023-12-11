from collections import Counter

from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip(), 5905),
]

CARDS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

REPOKER = 0
POKER = 1
FULL = 2
TRIO = 3
DOUBLE_PAIR = 4
PAIR = 5
HIGH_CARD = 6

"""
Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
"""


def cards_key(cards):
    return tuple(CARDS.index(card[0]) for card in cards)


def hand_key(hand):
    cards = Counter(hand)
    jokers = cards.pop('J', 0)
    if jokers:
        if jokers == 5:
            cards['A'] = 5
        best_card, best_count = max(cards.items(), key=lambda pair: pair[1])
        cards[best_card] += jokers

    if len(cards) == 1:
        return (REPOKER, cards_key(hand))
    elif len(cards) == 2:
        if 4 in cards.values():
            return (POKER, cards_key(hand))
        else:
            return (FULL, cards_key(hand))
    elif len(cards) == 3:
        if 3 in cards.values():
            return (TRIO, cards_key(hand))
        else:
            return (DOUBLE_PAIR, cards_key(hand))
    elif len(cards) == 4:
        return (PAIR, cards_key(hand))
    else:
        return (HIGH_CARD, cards_key(hand))


def solve(input):
    hands_with_bids = [line.split() for line in input.strip().split('\n')]
    sorted_hands = sorted(hands_with_bids, key=lambda pair: hand_key(pair[0]), reverse=True)
    winnings = 0
    for rank, (hand, bid) in enumerate(sorted_hands):
        print(rank + 1, hand, bid, hand_key(hand))
        winnings += int(bid) * (rank + 1)
    return winnings


if __name__ == '__main__':
    main(solve, TEST_CASES)
