from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip(), 114),
]


def extrapolate(numbers):
    last = []
    differences = numbers
    while any(d != 0 for d in differences):
        last.append(differences[-1])
        differences = [differences[i] - differences[i - 1] for i in range(1, len(differences))]
    return sum(last)


def solve(input):
    sum = 0
    for line in input.strip().split('\n'):
        numbers = [int(number) for number in line.split()]
        history = extrapolate(numbers)
        sum += history

    return sum


if __name__ == '__main__':
    main(solve, TEST_CASES)
