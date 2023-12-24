from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip(), 1030),
]


def solve(input):
    factor = (10 if input == TEST_CASES[0].case else 1000000) - 1
    galaxies = [
        (x, y)
        for y, line in enumerate(input.splitlines())
        for x, char in enumerate(line)
        if char == '#'
    ]
    double_rows = set(range(len(input.splitlines()))) - {y for _, y in galaxies}
    double_cols = set(range(len(input.splitlines()[0]))) - {x for x, _ in galaxies}

    total = 0
    for i, (x1, y1) in enumerate(galaxies):
        for x2, y2 in galaxies[i + 1:]:
            distance = abs(x1 - x2) + abs(y1 - y2)
            double_rows_in_path = double_rows.intersection(range(min(y1, y2) + 1, max(y1, y2)))
            double_cols_in_path = double_cols.intersection(range(min(x1, x2) + 1, max(x1, x2)))
            distance += factor * len(double_rows_in_path) + factor * len(double_cols_in_path)
            total += distance

    return total


if __name__ == '__main__':
    main(solve, TEST_CASES)
