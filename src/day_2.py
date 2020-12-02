import sys
from typing import List, Tuple


def part_one(values: List[Tuple[int, int, str, str]]) -> int:
    nbr_valid_password = 0
    for lower_limit, upper_limit, character, input_string in values:
        count = input_string.count(character)
        if lower_limit <= count and count <= upper_limit:
            nbr_valid_password += 1
    return nbr_valid_password


def test_part_one():
    print("Testing part one")
    values = [(1, 3, "a", "abcde"), (1, 3, "b", "cdefg"), (2, 9, "c", "ccccccccc")]
    result = part_one(values)
    if result == 2:
        print("  Passed")
    else:
        print("  Failed")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_part_one()
    else:
        pass