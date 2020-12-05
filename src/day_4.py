import sys
import re
from typing import List


def part_one(passports: List[str]) -> int:
    validations = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = 0
    for passport in passports:
        if all([passport_type in passport for passport_type in validations]):
            valid_passports += 1
    return valid_passports


def part_two(passports: List[str]) -> int:
    validations = [
        r"byr:((19[2-9]\d)|(200[0-2]))\s",
        r"iyr:20((1\d)|(20))\s",
        r"eyr:20((2\d)|(30))\s",
        r"hgt:((1(([5-8]\d)|(90))cm)|(((59)|(6\d)|(7[0-6]))in))\s",
        r"hcl:#[0-9a-f]{6}\s",
        r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\s",
        r"pid:\d{9}\s",
    ]
    valid_passports = 0
    for passport in passports:
        if all([re.search(valid, passport + " ") for valid in validations]):
            valid_passports += 1
    return valid_passports


def parse_input(filepath):
    with open(filepath, "r") as fp:
        return re.split(r"\n\s*\n", fp.read())


def test_part_one():
    print("testing part one")
    passports = parse_input("inputs/day_4_test_input.txt")
    result = part_one(passports)
    if result == 2:
        print("  passed")
    else:
        print("  failed")


def test_part_two():
    print("testing part two")
    invalid = parse_input("inputs/day_4_test_input_2.txt")
    inv_res = part_two(invalid)
    valid = parse_input("inputs/day_4_test_input_3.txt")
    v_res = part_two(valid)
    if inv_res == 0 and v_res == 4:
        print("  passed")
    else:
        print("  failed")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_part_one()
        test_part_two()
    else:
        input_string = parse_input("inputs/day_4_part_1.txt")
        result = part_one(input_string)
        print("Part 1 result: {}".format(result))
        # result = part_two(tree_chart)
        # print("Part 2 result: {}".format(result))
