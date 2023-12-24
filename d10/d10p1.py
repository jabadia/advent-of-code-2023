from colorama import Fore

from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
.....
.S-7.
.|.|.
.L-J.
.....
""".strip(), 4),
    TestCase("""
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip(), 8),
]

TILES = {
    '|': 'NS',
    '-': 'EW',
    'L': 'NE',
    'J': 'NW',
    '7': 'SW',
    'F': 'SE',
    '.': '',
    'S': 'NSWE',
}

OPPOSITE = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
}


CORNERS = str.maketrans({
    '7': "\N{BOX DRAWINGS HEAVY DOWN AND LEFT}",
    'F': "\N{BOX DRAWINGS HEAVY DOWN AND RIGHT}",
    'J': "\N{BOX DRAWINGS HEAVY UP AND LEFT}",
    'L': "\N{BOX DRAWINGS HEAVY UP AND RIGHT}",
    '-': "\N{BOX DRAWINGS HEAVY HORIZONTAL}",
    '|': "\N{BOX DRAWINGS HEAVY VERTICAL}",
})

def can_move(tileA, tileB, direction):
    return direction in TILES[tileA] and OPPOSITE[direction] in TILES[tileB]


def solve(input):
    map = [list(line) for line in input.strip().split('\n')]
    width = len(map[0])
    map = [['.'] * (width + 2)] + [['.'] + row + ['.'] for row in map] + [['.'] * (width + 2)]
    for j, row in enumerate(map):
        if 'S' in row:
            start = (row.index('S'), j)
            break

    # bfs
    queue = [(start, 0)]
    visited = set()
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if can_move(map[y][x], map[y - 1][x], 'N'):
            queue.append(((x, y - 1), steps + 1))
        if can_move(map[y][x], map[y + 1][x], 'S'):
            queue.append(((x, y + 1), steps + 1))
        if can_move(map[y][x], map[y][x + 1], 'E'):
            queue.append(((x + 1, y), steps + 1))
        if can_move(map[y][x], map[y][x - 1], 'W'):
            queue.append(((x - 1, y), steps + 1))

    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            tile = tile.translate(CORNERS)
            if (x, y) in visited:
                print(Fore.LIGHTBLUE_EX + tile, end='')
            elif tile == 'I':
                print(Fore.RED + tile, end='')
            else:
                print(Fore.WHITE + tile, end='')
        print()


    return steps - 1


if __name__ == '__main__':
    main(solve, TEST_CASES)
