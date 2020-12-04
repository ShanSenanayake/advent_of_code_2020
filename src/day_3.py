import sys
from typing import List


def part_one(tree_chart: List[List[bool]], slope) -> int:
    x_step, y_step = slope
    x = x_step
    y = y_step
    nbr_of_trees = 0
    for i in range(len(tree_chart)):
        if i != y:
            continue
        nbr_of_trees = nbr_of_trees + 1 if tree_chart[y][x] else nbr_of_trees
        x = (x + x_step) % len(tree_chart[i])
        y += y_step
    return nbr_of_trees


def parse_lines(lines: List[str]) -> List[List[bool]]:
    tree_chart = []
    for index, line in enumerate(lines):
        tree_chart.append([x == "#" for x in line.rstrip()])
    return tree_chart


def test_part_one():
    print("testing part one")
    tree_chart_string = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    result = part_one(parse_lines(tree_chart_string.split("\n")), (3, 1))
    if result == 7:
        print("  passed")
    else:
        print("  failed")


def test_part_two():
    print("testing part two")
    tree_chart_string = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    tree_chart = parse_lines(tree_chart_string.split("\n"))
    result = part_one(tree_chart, (1, 1))
    result *= part_one(tree_chart, (3, 1))
    result *= part_one(tree_chart, (5, 1))
    result *= part_one(tree_chart, (7, 1))
    result *= part_one(tree_chart, (1, 2))
    if result == 336:
        print("  passed")
    else:
        print("  failed")


def parse_input() -> List[List[bool]]:
    with open("inputs/day_3_part_1.txt", "r") as fp:
        return parse_lines(fp.readlines())


def part_two(tree_chart: List[List[bool]]):
    result = part_one(tree_chart, (1, 1))
    result *= part_one(tree_chart, (3, 1))
    result *= part_one(tree_chart, (5, 1))
    result *= part_one(tree_chart, (7, 1))
    result *= part_one(tree_chart, (1, 2))
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_part_one()
        test_part_two()
    else:
        tree_chart = parse_input()
        result = part_one(tree_chart, (3, 1))
        print("Part 1 result: {}".format(result))
        result = part_two(tree_chart)
        print("Part 2 result: {}".format(result))
