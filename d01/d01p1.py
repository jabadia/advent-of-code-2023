from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""", 142)
]


def solve(input):
    calibration = 0
    for line in input.strip().split('\n'):
        digits = [digit for digit in line if digit.isdigit()]
        value = int(digits[0] + digits[-1])
        calibration += value

    return calibration


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
