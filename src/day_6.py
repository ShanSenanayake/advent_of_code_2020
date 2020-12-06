import sys
import re
from typing import List


def part_one(answers: List[str]) -> int:
    return sum([len(set(re.sub(r"[^a-z]+", "", answer))) for answer in answers])


def part_two(answers: List[str]) -> int:
    all_answers = [
        (re.sub(r"[^a-z]+", "", answer), answer.count("\n")) for answer in answers
    ]
    total_answers = 0
    for group_answer, count in all_answers:
        total_answers += len(
            [
                answer
                for answer in set(group_answer)
                if group_answer.count(answer) == count + 1
            ]
        )
    return total_answers


def parse_input():
    with open("inputs/day_6_input.txt", "r") as fp:
        return re.split(r"\n\s*\n", fp.read())


def test_part_one():
    print("testing part one")
    answers = []
    with open("inputs/day_6_test.txt", "r") as fp:
        answers = re.split(r"\n\s*\n", fp.read())
    result = part_one(answers)
    if result == 11:
        print("  passed")
    else:
        print("  failed")


def test_part_two():
    print("testing part two")
    answers = []
    with open("inputs/day_6_test.txt", "r") as fp:
        answers = re.split(r"\n\s*\n", fp.read())
    result = part_two(answers)
    print(result)
    if result == 6:
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
        print(
            sum(
                [
                    len(set(re.sub(r"[^a-z]+", "", answer)))
                    for answer in re.split(
                        r"\n\s*\n", open("inputs/day_6_input.txt").read()
                    )
                ]
            )
        )
