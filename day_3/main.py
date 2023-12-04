
def check_symbol(char: str) -> bool:
    if (char == '.' or char.isdigit() or char == '\n'):
        return False
    return True


def parse_number(line:str, index: int, direction: bool) -> tuple[str, str]:
    # direction: 0 -> right to left; 1 -> left to right
    number: str = ""
    new_line: list[str] = list(line)

    while (index >= 0 and line[index] != '\n' and line[index].isdigit()):
        
        if (direction):
            number += line[index]
            new_line[index] = '.'
            index += 1
        else:
            number = line[index] + number
            new_line[index] = '.'
            index -= 1

    return number, "".join(new_line)


def check_horizontal(line: str, index: int = -1) -> tuple[str, str, str]:
    left_number: str = 0
    right_number: str = 0

    if (index == -1):
        # Scan the whole line
        for char_index in range(len(line)):

            left, right, line = check_horizontal(line, char_index)
            left_number = str(int(left_number) + int(left))
            right_number = str(int(right_number) + int(right))

    else:
        if (check_symbol(line[index])):
            # Scan only around specific index
            # Check left
            if (index-1 >= 0 and line[index-1].isdigit()):
                left_number, line = parse_number(line, index-1, False)

            # Check right
            if (line[index+1] != '\n' and line[index+1].isdigit()):
                right_number, line = parse_number(line, index+1, True)

    return left_number, right_number, line


def check_vertical(offset_line: str, line: str, reset: bool = False) -> tuple[int, str]:

    new_offset: list[str] = list(offset_line)
    offset_number: str = ""
    offset_sym: str = ""
    
    total_offset: int = 0
    left_number: str = "0"
    right_number: str = "0"

    for index, char in enumerate(line):

        if (check_symbol(char)):
            # Check the character offset directly adjacent
            if offset_line[index].isdigit():
                offset_number = offset_line[index]
            else:
                offset_sym = offset_line[index]
                offset_number = ""

            # Replace the character offset with a symbol to use for checking offset left and offset right spots
            offset_line = offset_line[:index] + "*" + offset_line[index+1:]
            left_number, right_number, offset_line = check_horizontal(offset_line, index)

            if reset:
                # If present, replace the original number (now *) with a . to avoid double counting
                # Otherwise replace the * with the original symbol present
                offset_line = offset_line[:index] + ("." if offset_number else offset_sym) + offset_line[index+1:]

            if offset_number:
                if left_number:
                    offset_number = left_number + offset_number
                if right_number:
                    offset_number = offset_number + right_number

                total_offset += int(offset_number)
            else:
                total_offset += int(left_number) + int(right_number)

    return total_offset, "".join(new_offset)


if __name__ == "__main__":

    lines: list[str]
    total: int = 0
    partial_left: str = "0"
    partial_right: str = "0"
    partial_offset: int = 0

    with open("day_3/input.txt", "r") as f:
        lines = f.readlines()

    for index, line in enumerate(lines):

        # Check horizontally for every line
        partial_left, partial_right, _ = check_horizontal(line)

        total += int(partial_left) + int(partial_right)

        if (index > 0):
            # If not on the top line, check above
            partial_offset, _ = check_vertical(lines[index-1], lines[index])
            total += partial_offset

        if (index + 1 < len(lines)):
            # If not on the last line, check below
            partial_offset, _ = check_vertical(lines[index+1], lines[index], reset=True)
            total += partial_offset

    print("Part 1:", total)