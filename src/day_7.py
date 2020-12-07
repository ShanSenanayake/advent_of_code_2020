import sys
import re
from typing import List, Set, Dict


def is_valid_rule(rule: str, bags: Set[str]) -> Set[str]:
    bag = rule.split("bags contain")[0]
    condition = rule.split("bags contain")[1]
    for b in bags:
        if b in condition:
            new_bags = set(bags)
            new_bags.add(bag)
            return new_bags
    return bags


def is_valid_rule_memo(rule: str, bags: Dict[str, int]):
    bag = rule.split(" bags contain")[0].rstrip()
    contained_bags = rule.split("contain")[1].split(",")
    contained_bags_keys = [
        re.search(r"(\d) ([a-z]+ [a-z]+)", b) for b in contained_bags
    ]
    if bag in bags:
        return
    for match in contained_bags_keys:
        if not match:
            return
        if match.group(2) not in bags:
            return
    bag_sum = 0
    for match in contained_bags_keys:
        nbr_bags = int(match.group(1))
        bag_sum += nbr_bags + nbr_bags * bags[match.group(2)]
    bags[bag] = bag_sum


def part_one(bag_rules: List[str]) -> int:
    nbr_of_bags = 0
    bags = set(["shiny gold"])
    while nbr_of_bags < len(bags):
        nbr_of_bags = len(bags)
        for rule in bag_rules:
            bags = is_valid_rule(rule, bags)
    return nbr_of_bags - 1


def part_two(bag_rules: List[str]) -> int:
    memo_bags = {}
    for rule in bag_rules:
        if "no other bags" in rule:
            bag = rule.split("bags contain")[0].rstrip()
            memo_bags[bag] = 0
    while len(memo_bags) < len(bag_rules):
        for rule in bag_rules:
            is_valid_rule_memo(rule, memo_bags)
    return memo_bags["shiny gold"]


def parse_input():
    with open("inputs/day_7_input.txt", "r") as fp:
        return fp.readlines()


def test_part_one():
    print("testing part one")
    answers = []
    with open("inputs/day_7_test.txt", "r") as fp:
        answers = fp.readlines()
    result = part_one(answers)
    if result == 4:
        print("  passed")
    else:
        print("  failed")


def test_part_two():
    print("testing part two")
    answers = []
    with open("inputs/day_7_test_2.txt", "r") as fp:
        answers = fp.readlines()
    result = part_two(answers)
    if result == 126:
        print("  passed")
    else:
        print("  failed")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_part_one()
        test_part_two()
    else:
        input_list = parse_input()
        result = part_one(input_list)
        print("Part 1 result: {}".format(result))
        result = part_two(input_list)
        print("Part 2 result: {}".format(result))