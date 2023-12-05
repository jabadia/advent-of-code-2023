from utils.main import main
from utils.test_case import TestCase
import re

TEST_CASES = [
    TestCase("""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip(), 13),
]


def evaluate_card(card):
    card_id, numbers = [s.strip() for s in card.split(':')]
    winning_numbers, my_numbers = [s.strip() for s in numbers.split('|')]
    winning_numbers = set(int(s) for s in re.split('\s+', winning_numbers))
    my_numbers = set(int(s) for s in re.split('\s+', my_numbers))
    return int(2 ** (len(winning_numbers.intersection(my_numbers)) - 1))


def solve(input):
    total = 0
    for card in input.strip().split('\n'):
        total += evaluate_card(card)
    return total


if __name__ == '__main__':
    main(solve, TEST_CASES)

