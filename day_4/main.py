import re


def count_points(line: str) -> int:
    
    points_total: int = 0
    
    line = re.sub("Card +[0-9]*: *", "", line)  # Remove leading text and space
    line = re.sub(" +", " ", line)              # Unify spacing to be only one long between numbers
    line = line.replace('\n', '')               # Remove trailing EOL character

    winning_numbers: list[str] = line.split(' |')[0].split(' ')
    candidates: list[str] = line.split('| ')[1].split(' ')

    for number in candidates:
    
        if number in winning_numbers:
            if (points_total == 0):
                points_total = 1
            else:
                points_total *= 2

    return points_total


if __name__ == "__main__":
    total_one: int = 0
    with open("day_4/input.txt", "r") as f:
        for line in f.readlines():
            total_one += count_points(line)

    print("Part 1:", total_one)
