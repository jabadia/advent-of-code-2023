import itertools
import re

from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip(), 21),
]


def is_matching(row, numbers):
    springs = [len(damaged_group) for damaged_group in re.split(r'\.+', row) if damaged_group]
    # print(row, springs)
    return springs == numbers


def solve(input):
    valid = 0
    for i, line in enumerate(input.strip().split('\n')):
        row, numbers = line.split()
        print(i, row, numbers)
        numbers = [int(n) for n in numbers.split(',')]
        placeholders = row.count('?')
        for alternative in itertools.product('.#', repeat=placeholders):
            if is_matching(row.replace('?', '{}').format(*alternative), numbers):
                valid += 1
    return valid


if __name__ == '__main__':
    main(solve, TEST_CASES)
