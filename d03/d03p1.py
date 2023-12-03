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
""".strip(), 4361),
]


def has_neighbour_symbol(rows, i, j):
    for offset_j in range(-1, 2):
        for offset_i in range(-1, 2):
            if offset_i == offset_j == 0:
                continue
            if 0 < j + offset_j < len(rows) - 1 and 0 < i + offset_i < len(rows[0]) - 1:
                char = rows[j + offset_j][i + offset_i]
                if char != '.' and not char.isdigit():
                    return True


def solve(input):
    part_numbers_sum = 0
    rows = input.strip().split('\n')
    for j, row in enumerate(rows):
        current_number = ''
        current_is_part = False
        for i, char in enumerate(row):
            if char.isdigit():
                current_number += char
                if has_neighbour_symbol(rows, i, j):
                    current_is_part = True
            elif current_number:
                print(current_number, current_is_part)
                if current_is_part:
                    part_numbers_sum += int(current_number)
                current_number = ''
                current_is_part = False
        if current_number and current_is_part:
            part_numbers_sum += int(current_number)
    return part_numbers_sum


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
