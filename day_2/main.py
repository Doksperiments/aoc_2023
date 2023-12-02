import re

RED_LIMIT: int = 12
GREEN_LIMIT: int = 13
BLUE_LIMIT: int = 14

def format_line(line: str) -> tuple[int, list[dict[str, int]]]:

    index: int
    search: re.Match[str] | None
    values: dict[str, int] = dict()
    values_list: list[dict[str, int]] = list()

    if search := re.search("Game ([0-9]+):", line):
        index = int(search.group(1))
    else:
        raise ValueError("No game index found")
    

    for group in line.split(": ")[1].split("; "):

        for pair in group.split(","):
            if search := re.search("([0-9]+) red", pair):
                values["red"] = int(search.group(1)) if search.group(1) else 0
            if search := re.search("([0-9]+) green", pair):
                values["green"] = int(search.group(1)) if search.group(1) else 0
            if search := re.search("([0-9]+) blue", pair):
                values["blue"] = int(search.group(1)) if search.group(1) else 0

        values_list.append(values)
        values = dict()

    fmt_line: tuple[int, list[dict[str, int]]] = (index, values_list)
    return fmt_line

def filter_max(line: tuple[int, list[dict[str, int]]]) -> tuple[int, tuple[int, int, int]]:

    red_max: int = 0
    green_max: int = 0
    blue_max: int = 0

    for pairs in line[1]:
        if "red" in pairs.keys():
            red_max = max(pairs["red"], red_max)
        if "green" in pairs.keys():
            green_max = max(pairs["green"], green_max)
        if "blue" in pairs.keys():
            blue_max = max(pairs["blue"], blue_max)

    filtered_list: tuple[int, tuple[int, int, int]] = (line[0], (red_max, green_max, blue_max))

    return filtered_list

def check_limit(line: tuple[int, tuple[int, int, int]]) -> bool:

    return (line[1][0] <= RED_LIMIT) and (line[1][1] <= GREEN_LIMIT) and (line[1][2] <= BLUE_LIMIT)

def calculate_power(line: tuple[int, tuple[int, int, int]]) -> int:
    return line[1][0] * line[1][1] * line[1][2]

if __name__ == "__main__":
    total_one: int = 0
    total_two: int = 0

    with open("day_2/input.txt", "r") as f:
        for line in f.readlines():
            line = format_line(line)
            line = filter_max(line)
            total_one += check_limit(line) * line[0]
            total_two += calculate_power(line)

    print("Part 1:", total_one)
    print("Part 2:", total_two)
