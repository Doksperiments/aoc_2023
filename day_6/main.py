import re


def get_line_values(line: str) -> list[int]:

    line = re.sub("[A-z]*: *", "", line)    # Remove leading text and space
    line = re.sub(" +", " ", line)          # Unify spacing to be only one long between numbers
    line = line.replace('\n', '')           # Remove trailing EOL character

    return [int(num) for num in line.split(' ')]


def calculate_charges(time: int) -> list[int]:
    return [(time-charge)*charge for charge in range(1, time)]


def filter_records(charges: list[int], distance: int) -> int:

    counter: int = 0

    for charge in charges:
        if charge > distance:
            counter += 1

    return counter


if __name__ == "__main__":
    
    times: list[int]
    distances: list[int]
    ways: int = 1

    with open("day_6/input.txt", "r") as f:
        times = get_line_values(f.readline())
        distances = get_line_values(f.readline())

    for (time, distance) in zip(times, distances):
        ways *= filter_records(calculate_charges(time), distance)

    print("Part 1:", ways)