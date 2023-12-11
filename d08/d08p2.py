import itertools
import math

from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip(), 6),
]


def solve(input):
    instructions, graph = input.strip().split('\n\n')
    graph = dict(line.split(' = ') for line in graph.split('\n'))
    graph = {key: value[1:-1].split(', ') for key, value in graph.items()}

    nodes = [node for node in graph.keys() if node[2] == 'A']
    all_steps = []

    for node in nodes:
        steps = 0
        for instruction in itertools.cycle(*instructions.split()):
            steps += 1
            if instruction == 'L':
                node = graph[node][0]
            elif instruction == 'R':
                node = graph[node][1]

            if node[2] == 'Z':
                all_steps.append(steps)
                break

    return math.lcm(*all_steps)


if __name__ == '__main__':
    main(solve, TEST_CASES)
