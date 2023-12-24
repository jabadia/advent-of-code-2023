from colorama import Fore
from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".strip(), 4),
    TestCase("""
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".strip(), 8),
    TestCase("""
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".strip(), 10),
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


def can_move(map, x, y, direction):
    tileA = map[y][x]
    if direction == 'N':
        tileB = map[y - 1][x]
    elif direction == 'S':
        tileB = map[y + 1][x]
    elif direction == 'E':
        tileB = map[y][x + 1]
    elif direction == 'W':
        tileB = map[y][x - 1]
    return direction in TILES[tileA] and OPPOSITE[direction] in TILES[tileB]


def solve(input):
    map = [list(line) for line in input.strip().split('\n')]
    width = len(map[0])
    map = [['.'] * (width + 2)] + [['.'] + row + ['.'] for row in map] + [['.'] * (width + 2)]
    for y, row in enumerate(map):
        if 'S' in row:
            x = row.index('S')
            start = (x, y)
            break

    # bfs
    queue = [(start, 0)]
    visited = set()
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if can_move(map, x, y, 'N'):
            queue.append(((x, y - 1), steps + 1))
        if can_move(map, x, y, 'S'):
            queue.append(((x, y + 1), steps + 1))
        if can_move(map, x, y, 'E'):
            queue.append(((x + 1, y), steps + 1))
        if can_move(map, x, y, 'W'):
            queue.append(((x - 1, y), steps + 1))

    # close loop at start
    start_directions = {
        direction
        for direction in ['N', 'S', 'E', 'W']
        if can_move(map, start[0], start[1], direction)
    }

    for tile, tile_directions in TILES.items():
        if start_directions == set(tile_directions):
            map[start[1]][start[0]] = tile
            break

    # find inside area
    area = 0
    for y, row in enumerate(map):
        inside = False
        x = 0
        horizontal_start = None
        while x < len(row):
            tile = row[x]
            if (x, y) in visited and tile in ('L', 'F'):  # begin horizontal line
                horizontal_start = tile
            elif (x, y) in visited and tile in ('7', 'J'):  # end horizontal line
                assert horizontal_start is not None
                if tile == '7' and horizontal_start == 'L' or tile == 'J' and horizontal_start == 'F':
                    inside = not inside
                horizontal_start = None
            elif (x, y) in visited and tile == '|':
                inside = not inside
            elif (x, y) not in visited and inside:
                map[y][x] = 'I'
                area += 1
            x += 1

    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            tile = tile.translate(CORNERS)
            if (x, y) == start:
                print(Fore.LIGHTYELLOW_EX + tile, end='')
            elif (x, y) in visited:
                print(Fore.LIGHTBLUE_EX + tile, end='')
            elif tile == 'I':
                print(Fore.RED + tile, end='')
            else:
                print(Fore.WHITE + tile, end='')
        print()

    return area


if __name__ == '__main__':
    main(solve, TEST_CASES)
