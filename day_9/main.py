
def split_line(line: str) -> list[int]:
    line = line.removesuffix('\n')

    return [int(num) for num in line.split(' ')]


def extrapolate_right(values: list[int]) -> int:

    if all(value == 0 for value in values):
        return 0
    else:
        return values[-1] + extrapolate_right([right - left for left, right in zip(values, values[1:])])


def extrapolate_left(values: list[int]) -> int:

    if all(value == 0 for value in values):
        return 0
    else:
        return values[0] - extrapolate_left([right - left for left, right in zip(values, values[1:])])


if __name__ == "__main__":

    lines: list[str]

    with open("day_9/input.txt", "r") as f:
        lines = f.readlines()

    print("Part 1:", sum([extrapolate_right(split_line(line)) for line in lines]))
    print("Part 2:", sum([extrapolate_left(split_line(line)) for line in lines]))
