
def replace_digit(line: str):
    
    i: int = 0

    while (i < len(line) and line[i] != '\n'):
        
        ch: str = line[i]

        match ch:
            case 'o':
                if line[i:i+3] == "one":
                    line = line.replace("one", "1ne", 1)
                    i += 1
                else:
                    line = line.replace(ch, '', 1)

            case 't':
                if line[i:i+3] == "two":
                    line = line.replace("two", "2wo", 1)
                    i += 1
                elif line[i:i+5] == "three":
                    line = line.replace("three", "3hree", 1)
                    i += 1
                else:
                    line = line.replace(ch, '', 1)
                
            case 'f':
                if line[i:i+4] == "four":
                    line = line.replace("four", "4our", 1)
                    i += 1
                elif line[i:i+4] == "five":
                    line = line.replace("five", "5ive", 1)
                    i += 1
                else:
                    line = line.replace(ch, '', 1)
                
            case 's':
                if line[i:i+3] == "six":
                    line = line.replace("six", "6ix", 1)
                    i += 1
                elif line[i:i+5] == "seven":
                    line = line.replace("seven", "7even", 1)
                    i += 1
                else:
                    line = line.replace(ch, '', 1)
                
            case 'e':
                if line[i:i+5] == "eight":
                    line = line.replace("eight", "8ight", 1)
                    i += 1
                else:
                    line = line.replace(ch, '', 1)
                
            case 'n':
                if line[i:i+4] == "nine":
                    line = line.replace("nine", "9ine", 1)
                    i += 1
                else:
                    line = line.replace(ch, '', 1)
                
            case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
                # Ignore actual digits
                i += 1
            case _:
                # Remove other characters
                line = line.replace(ch, '', 1)

    return line


def extract_calibration(line: str) -> int:

    digit: int = 0
    line = replace_digit(line)

    digit += 10 * int(line[0])
    digit += int(line[-2])
    return digit


if __name__ == "__main__":
    total: int = 0
    with open("day_1/input.txt", "r") as f:
        for line in f.readlines():
            total += extract_calibration(line)

        print(total)
