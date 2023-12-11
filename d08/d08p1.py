import itertools

from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip(), 2),
    TestCase("""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip(), 6),
]


def solve(input):
    instructions, graph = input.strip().split('\n\n')
    graph = dict(line.split(' = ') for line in graph.split('\n'))
    graph = {key: value[1:-1].split(', ') for key, value in graph.items()}

    node = 'AAA'
    steps = 0
    for instruction in itertools.cycle(*instructions.split()):
        steps += 1
        if instruction == 'L':
            node = graph[node][0]
        elif instruction == 'R':
            node = graph[node][1]

        if node == 'ZZZ':
            return steps


if __name__ == '__main__':
    main(solve, TEST_CASES)
