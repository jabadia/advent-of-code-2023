from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""", 142),
    TestCase("""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""", 281)
]

digit_names = ['___', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def solve(input):
    calibration = 0
    for line in input.strip().split('\n'):
        first_digit = None
        last_digit = None
        for pos in range(len(line)):
            for digit, digit_name in enumerate(digit_names):
                if line[pos:].startswith(digit_name) or line[pos] == str(digit):
                    if first_digit is None:
                        first_digit = digit
                    last_digit = digit
        value = first_digit * 10 + last_digit
        calibration += value

    return calibration


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        if not case.check(result):
            exit(1)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
