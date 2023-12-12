from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip(), 2),
]


def extrapolate(numbers):
    first = []
    differences = numbers
    while any(d != 0 for d in differences):
        first.append(differences[0])
        differences = [differences[i] - differences[i - 1] for i in range(1, len(differences))]

    return sum(first[::2]) - sum(first[1::2])


def solve(input):
    sum = 0
    for line in input.strip().split('\n'):
        numbers = [int(number) for number in line.split()]
        history = extrapolate(numbers)
        sum += history

    return sum


if __name__ == '__main__':
    main(solve, TEST_CASES)
