from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
Time:      7  15   30
Distance:  9  40  200
""".strip(), 288),
]


def evaluate_race(time, record):
    ways = 0
    last_distance = 0
    for i in range(time):
        distance = i * (time - i)
        if distance > record:
            ways += 1
        if distance < last_distance and distance <= record:
            break
        last_distance = distance
    return ways


def solve(input):
    races = zip(*[(int(number) for number in line.split(':')[1].split()) for line in input.strip().split('\n')])
    number_of_ways = 1
    for time, record in races:
        number_of_ways *= evaluate_race(time, record)
    return number_of_ways


if __name__ == '__main__':
    main(solve, TEST_CASES)
