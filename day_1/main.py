def extract_calibration(line: str) -> int:

    digit: int = 0

    for ch in line:
        if (ch >= '0' and ch <= '9'):
            digit += 10 * int(ch)
            break

    for ch in line[::-1]:
        if (ch >= '0' and ch <= '9'):
            digit += int(ch)
            break

    return digit


if __name__ == "__main__":
    total: int = 0
    with open("day_1/input.txt", "r") as f:
        for line in f.readlines():
            total += extract_calibration(line)

        print(total)
