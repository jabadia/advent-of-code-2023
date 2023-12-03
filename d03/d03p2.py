from collections import defaultdict

from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip(), 467835),
]


def find_neighbour_gear(rows, i, j):
    for offset_j in range(-1, 2):
        for offset_i in range(-1, 2):
            if offset_i == offset_j == 0:
                continue
            if 0 < j + offset_j < len(rows) - 1 and 0 < i + offset_i < len(rows[0]) - 1:
                char = rows[j + offset_j][i + offset_i]
                if char == '*':
                    return i + offset_i, j + offset_j


def solve(input):
    rows = input.strip().split('\n')
    gears = defaultdict(list)
    for j, row in enumerate(rows):
        current_number = ''
        neighbour_gears = set()
        for i, char in enumerate(row):
            if char.isdigit():
                current_number += char
                neighbour_gears.add(find_neighbour_gear(rows, i, j))
            elif current_number:
                for gear in neighbour_gears:
                    if gear:
                        gears[gear].append(int(current_number))
                current_number = ''
                neighbour_gears = set()
        if current_number:
            for gear in neighbour_gears:
                if gear:
                    gears[gear].append(int(current_number))

    ratio_sum = 0
    for gear, parts in gears.items():
        if len(parts) == 2:
            ratio_sum += parts[0] * parts[1]
        else:
            print(gear, parts)
    return ratio_sum


if __name__ == '__main__':
    input = fetch_input()
    fails = 0
    for case in TEST_CASES:
        result = solve(case.case)
        if not case.check(result):
            fails += 1

    if not fails:
        answer = solve(input)
        print(answer)
        submit_answer(answer)
