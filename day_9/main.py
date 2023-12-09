
def split_line(line: str) -> list[int]:
    line = line.removesuffix('\n')

    return [int(num) for num in line.split(' ')]


def extrapolate_value(values: list[int]) -> int:

    if sum(values) == 0:    # All elements must be 0 since they can't be < 0
        return 0
    else:
        return values[-1] + extrapolate_value([right - left for left, right in zip(values, values[1:])])


if __name__ == "__main__":

    lines: list[str]

    with open("day_9/input.txt", "r") as f:
        lines = f.readlines()


    print("Part 1:", sum([extrapolate_value(split_line(line)) for line in lines]))
