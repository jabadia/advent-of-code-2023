from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer


def main(solve, TEST_CASES):
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
