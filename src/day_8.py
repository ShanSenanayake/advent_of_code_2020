import sys
from typing import List, Tuple


def parse_instruction(instruction: str) -> Tuple[str, int]:
    cmd, value = instruction.split(" ")
    return (cmd.rstrip(), int(value))


def part_one(instructions: List[str]) -> int:
    visited = set()
    next_index = 0
    acc = 0
    while next_index not in visited:
        visited.add(next_index)
        cmd, value = parse_instruction(instructions[next_index])
        if cmd == "acc":
            acc += value
            next_index += 1
        elif cmd == "nop":
            next_index += 1
        else:
            next_index += value
    return acc


def part_two(instructions: List[str]) -> int:
    visited = set()
    rollback_visited = set()
    rollback_acc = 0
    rollback_next_index = 0
    has_changed = False
    next_index = 0
    acc = 0
    while next_index < len(instructions):
        rolled_back = False
        if next_index in visited:
            # rollback
            visited = rollback_visited
            acc = rollback_acc
            next_index = rollback_next_index
            has_changed = False
            rolled_back = True
        cmd, value = parse_instruction(instructions[next_index])
        if (
            cmd == "nop"
            and not has_changed
            and not rolled_back
            and next_index + value < len(instructions) + 1
        ):
            cmd = "jmp"
            has_changed = True
            rollback_visited = set(visited)
            rollback_acc = acc
            rollback_next_index = next_index
        elif cmd == "jmp" and not has_changed and not rolled_back:
            cmd = "nop"
            has_changed = True
            rollback_visited = set(visited)
            rollback_acc = acc
            rollback_next_index = next_index
        visited.add(next_index)
        if cmd == "acc":
            acc += value
            next_index += 1
        elif cmd == "nop":
            next_index += 1
        else:
            next_index += value
        if next_index > len(instructions) + 1:
            next_index = 0
    return acc


def parse_input():
    with open("inputs/day_8_input.txt", "r") as fp:
        return fp.readlines()


def test_part_one():
    print("testing part one")
    answers = []
    with open("inputs/day_8_test.txt", "r") as fp:
        answers = fp.readlines()
    result = part_one(answers)
    if result == 5:
        print("  passed")
    else:
        print("  failed")


def test_part_two():
    print("testing part two")
    answers = []
    with open("inputs/day_8_test.txt", "r") as fp:
        answers = fp.readlines()
    result = part_two(answers)
    if result == 8:
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