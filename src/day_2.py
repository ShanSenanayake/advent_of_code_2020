import sys
from typing import List, Tuple


def part_one(values: List[Tuple[int, int, str, str]]) -> int:
    nbr_valid_password = 0
    for lower_limit, upper_limit, character, input_string in values:
        count = input_string.count(character)
        if lower_limit <= count and count <= upper_limit:
            nbr_valid_password += 1
    return nbr_valid_password


def part_two(values: List[Tuple[int, int, str, str]]) -> int:
    nbr_valid_password = 0
    for first_index, second_index, character, input_string in values:
        # No need to shift since the parsing has an extra empty space char
        first_position = input_string[first_index] == character
        second_position = input_string[second_index] == character
        if first_position != second_position:
            nbr_valid_password += 1
    return nbr_valid_password


def test_part_one():
    print("Testing part one")
    values = [(1, 3, "a", " abcde"), (1, 3, "b", " cdefg"), (2, 9, "c", " ccccccccc")]
    result = part_one(values)
    if result == 2:
        print("  Passed")
    else:
        print("  Failed")


def test_part_two():
    print("Testing part two")
    values = [(1, 3, "a", " abcde"), (1, 3, "b", " cdefg"), (2, 9, "c", " ccccccccc")]
    result = part_two(values)
    if result == 1:
        print("  Passed")
    else:
        print("  Failed")


def parse_input() -> List[Tuple[int, int, str, str]]:
    result: List = []
    with open("inputs/day_2_part_1.txt", "r") as fp:
        for line in fp.readlines():
            rules, input_string = line.split(":")
            limits, character = rules.split(" ")
            lower_limit, upper_limit = [int(limit) for limit in limits.split("-")]
            result.append((lower_limit, upper_limit, character, input_string))
        return result


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_part_one()
        test_part_two()
    else:
        input_values = parse_input()
        result = part_one(input_values)
        print("Part 1 result: {}".format(result))
        result = part_two(input_values)
        print("Part 2 result: {}".format(result))