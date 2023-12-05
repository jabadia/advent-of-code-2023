from itertools import chain
from utils.asserts import assert_equal

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
""".strip(), 46),
]


def remove_empty(ranges):
    return [(start, end) for start, end in ranges if start != end]


def overlap(seed_range, map_range):  # returns overlapping, [non-overlapping ranges]
    seed_start, seed_end = seed_range
    map_start, map_end = map_range
    if seed_end <= map_start:
        return None, [seed_range]
    if map_end <= seed_start:
        return None, [seed_range]
    if seed_start <= map_start and map_end <= seed_end:
        return map_range, remove_empty([(seed_start, map_start), (map_end, seed_end)])
    if map_start <= seed_start and seed_end <= map_end:
        return seed_range, []
    if map_start <= seed_end <= map_end:
        return (map_start, seed_end), [(seed_start, map_start)]
    if map_start <= seed_start <= map_end:
        return (seed_start, map_end), [(map_end, seed_end)]
    assert False


assert_equal(overlap((0, 10), (0, 10)), ((0, 10), []))
assert_equal(overlap((1, 9), (0, 10)), ((1, 9), []))
assert_equal(overlap((0, 10), (10, 15)), (None, [(0, 10)]))
assert_equal(overlap((5, 10), (0, 15)), ((5, 10), []))
assert_equal(overlap((0, 15), (5, 10)), ((5, 10), [(0, 5), (10, 15)]))
assert_equal(overlap((0, 10), (5, 15)), ((5, 10), [(0, 5)]))
assert_equal(overlap((5, 15), (0, 10)), ((5, 10), [(10, 15)]))
print('## [INFO] all tests passed')


def solve(input):
    maps = input.strip().split('\n\n')
    seed_map = maps[0]
    seeds = [int(s) for s in seed_map.split(':')[1].strip().split()]
    print(seeds)
    seed_ranges = {(start, start + end) for start, end in zip(seeds[::2], seeds[1::2])}
    print(seed_ranges)
    for map in maps[1:]:
        next_seed_ranges = set()
        lines = map.strip().split('\n')
        map_name = lines[0].split(':')[0].strip()
        print(map_name)
        for line in lines[1:]:
            destination_start, source_start, range_length = [int(s) for s in line.split()]
            for seed_range in seed_ranges.copy():
                # calculate overlap and map to new range
                # copy the rest
                seed_ranges.remove(seed_range)
                overlap_range, non_overlapping = overlap(seed_range, (source_start, source_start + range_length))
                if overlap_range:
                    next_seed_ranges.add((
                        destination_start - source_start + overlap_range[0],
                        destination_start - source_start + overlap_range[1]
                    ))
                seed_ranges |= set(non_overlapping)
        seed_ranges |= next_seed_ranges
        print(sorted(seed_ranges))
    return min(start for start, end in seed_ranges)


if __name__ == '__main__':
    main(solve, TEST_CASES)
