import sys
from typing import List, Set


def find_terms(terms: Set[int]) -> (int, int):
    for term in terms:
        complement_term = 2020 - term
        if complement_term in terms:
            return (term, complement_term)


def part_one(values: List[int]) -> int:
    factors = find_terms(set(values))
    return factors[0] * factors[1]


def test_part_one():
    print("Testing part one")
    values = [1721, 979, 366, 299, 675, 1456]
    result = part_one(values)
    if result == 514579:
        print("  Passed")
    else:
        print("  Failed")


def parse_input() -> List[int]:
    result: List = None
    with open("inputs/day_1_part_1.txt", "r") as fp:
        result = [int(line) for line in fp.readlines()]
        return result


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_part_one()
    else:
        input_values = parse_input()
        result = part_one(input_values)
        print("Part 1 result: {}".format(result))
