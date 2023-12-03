from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1),
    TestCase("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 2),
    TestCase("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 0),
    TestCase("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 0),
    TestCase("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 5),
]

bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def is_possible(game):
    game_id, subsets = (s.strip() for s in game.split(':'))
    game_id = int(game_id[5:])
    for subset in subsets.split(';'):
        for cube in subset.split(','):
            count, color = cube.strip().split(' ')
            if bag[color] < int(count):
                return 0

    return game_id


def solve(input):
    return sum(is_possible(game.strip()) for game in input.strip().split('\n'))


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
