from utils.test_case import TestCase
from utils.main import main

TEST_CASES = [
    TestCase("""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip(), 35),
]


def solve(input):
    maps = input.strip().split('\n\n')
    seed_map = maps[0]
    seeds = {int(s) for s in seed_map.split(':')[1].strip().split()}
    print(seeds)
    for map in maps[1:]:
        next_seeds = set()
        lines = map.strip().split('\n')
        map_name = lines[0].split(':')[0].strip()
        print(map_name)
        for line in lines[1:]:
            destination_start, source_start, range_length = [int(s) for s in line.split()]
            for seed in seeds.copy():
                if source_start <= seed < source_start + range_length:
                    next_seeds.add(destination_start + seed - source_start)
                    seeds.remove(seed)
        next_seeds |= seeds
        seeds = next_seeds
    return min(seeds)


if __name__ == '__main__':
    main(solve, TEST_CASES)
