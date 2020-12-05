import sys
from typing import List, Tuple


def find_seat(search_string: str, start_value: int, condition: str) -> int:
    result = 0
    for i in search_string:
        start_value = start_value / 2
        if i == condition:
            result += start_value
    return int(result)


def calc_id(boarding_pass: str) -> int:
    row = find_seat(boarding_pass[:-3], 128, "B")
    column = find_seat(boarding_pass[7:], 8, "R")
    return row * 8 + column


def get_seat(boarding_pass: str) -> Tuple[int, int, int]:
    row = find_seat(boarding_pass[:-3], 128, "B")
    column = find_seat(boarding_pass[7:], 8, "R")
    return (row, column, row * 8 + column)


def part_one(passes: List[str]) -> int:
    return max([calc_id(p) for p in passes])


def part_two(passes: List[str]) -> int:
    seating_matrix = [[0 for _ in range(8)] for _ in range(128)]
    seat_ids = set()
    for row, col, id in [get_seat(p) for p in passes]:
        seating_matrix[row][col] = id
        seat_ids.add(id)
    for row_i, row in enumerate(seating_matrix):
        for col_i, id in enumerate(row):
            seat_id = row_i * 8 + col_i
            if id == 0 and (seat_id + 1) in seat_ids and (seat_id - 1) in seat_ids:
                return seat_id


def parse_input():
    with open("inputs/day_5_part_1.txt", "r") as fp:
        return [line.rstrip() for line in fp.readlines()]


def test_part_one():
    print("testing part one")
    passes = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL", "FBFBBFFRLR"]
    result = part_one(passes)
    if result == 820:
        print("  passed")
    else:
        print("  failed")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_part_one()
    else:
        input_list = parse_input()
        result = part_one(input_list)
        print("Part 1 result: {}".format(result))
        result = part_two(input_list)
        print("Part 2 result: {}".format(result))
