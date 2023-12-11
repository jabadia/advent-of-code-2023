import math

from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
Time:      7  15   30
Distance:  9  40  200
""".strip(), 71503),
]


def evaluate_race(time, record):
    t0 = (time - math.sqrt(time * time - 4 * record)) / 2
    t1 = (time + math.sqrt(time * time - 4 * record)) / 2
    return int(math.floor(t1) - math.ceil(t0) + 1)


def solve(input):
    races = zip(*[
        (int(number) for number in line.split(':')[1].split())
        for line in input.strip().replace(' ', '').split('\n')
    ])
    number_of_ways = 1
    for time, record in races:
        number_of_ways *= evaluate_race(time, record)
    return number_of_ways


if __name__ == '__main__':
    main(solve, TEST_CASES)
