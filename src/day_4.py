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


def parse_input(filepath):
    with open(filepath, "r") as fp:
        return fp.read()


def test_part_one():
    print("testing part one")
    input_string = parse_input("inputs/day_4_test_input.txt")
    passports = re.split(r"\n\s*\n", input_string)
    result = part_one(passports)
    if result == 2:
        print("  passed")
    else:
        print("  failed")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_part_one()
