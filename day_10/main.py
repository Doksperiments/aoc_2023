
def find_starting_point() -> tuple[int, int]:

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i, j

    return -1, -1


def start(row: int, col: int) -> int:

    if (row < len(grid)-1 and grid[row+1][col] in ("L", "J", "|")):
        return move("top", row+1, col)
    elif (row > 0 and grid[row-1][col] in ("F", "7", "|")):
        return move("bottom", row-1, col)
    elif (col < len(grid[0])-1 and grid[row][col+1] in ("7", "J", "-")):
        return move("left", row, col+1)
    elif (col > 0 and grid[row][col-1] in ("L", "F", "-")):
        return move("right", row, col-1)
    
    return -1


def move(prev_direction: str, row: int, col: int) -> int:

    steps: int = 0

    while (grid[row][col] != "S"):

        match grid[row][col]:
                case "L":
                    if prev_direction == "top":
                        prev_direction = "left"
                        col += 1
                    elif prev_direction == "right":
                        prev_direction = "bottom"
                        row -= 1
                    else:
                        raise Exception("Invalid direction")
                case "7":
                    if prev_direction == "left":
                        prev_direction = "top"
                        row += 1
                    elif prev_direction == "bottom":
                        prev_direction = "right"
                        col -= 1
                    else:
                        raise Exception("Invalid direction")
                case "J":
                    if prev_direction == "top":
                        prev_direction = "right"
                        col -= 1
                    elif prev_direction == "left":
                        prev_direction = "bottom"
                        row -= 1
                    else:
                        raise Exception("Invalid direction")
                case "F":
                    if prev_direction == "right":
                        prev_direction = "top"
                        row += 1
                    elif prev_direction == "bottom":
                        prev_direction = "left"
                        col += 1
                    else:
                        raise Exception("Invalid direction")
                case "|":
                    if prev_direction == "top":
                        row += 1
                    elif prev_direction == "bottom":
                        row -= 1
                    else:
                        raise Exception("Invalid direction")
                case "-":
                    if prev_direction == "left":
                        col += 1
                    elif prev_direction == "right":
                        col -= 1
                    else:
                        raise Exception("Invalid direction")
                case ".":
                    raise Exception("Not a loop")
                case _:
                    raise Exception("Unknown character")

        steps += 1

    return steps


if __name__ == "__main__":

    grid: list[list[str]] = []

    with open("day_10/input.txt", "r") as f:
        for line in f.readlines():
            grid.append([*line.removesuffix('\n')])

    print("Part 1:", (start(*find_starting_point())//2) + 1)
