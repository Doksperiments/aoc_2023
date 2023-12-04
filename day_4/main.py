import re

type card_type = tuple[list[str], list[str]]


def get_formatted_card(line: str) -> card_type:

    winning_numbers: list[str]
    candidates: list[str]
    
    line = re.sub("Card +[0-9]*: *", "", line)  # Remove leading text and space
    line = re.sub(" +", " ", line)              # Unify spacing to be only one long between numbers
    line = line.replace('\n', '')               # Remove trailing EOL character

    winning_numbers = line.split(' |')[0].split(' ')
    candidates = line.split('| ')[1].split(' ')

    return winning_numbers, candidates


def count_points(card: card_type) -> tuple[int, int]:
    
    points_total: int = 0
    matches_found: int = 0

    for number in card[1]:
    
        if number in card[0]:
            matches_found += 1
            if (points_total == 0):
                points_total = 1
            else:
                points_total *= 2

    return matches_found, points_total


def count_scratchcards(index: int, total_depth: int) -> int:

    total: int = 0

    for depth in range(total_depth):
        if (index+depth+1 < len(formatted_cards)):
            total += cards_values[index+depth+1]

    return 1 + total


if __name__ == "__main__":

    total_one: int = 0
    total_two: int = 0
    formatted_cards: list[card_type]
    cards_values: list[int]

    with open("day_4/input.txt", "r") as f:
        lines = f.readlines()

    formatted_cards = [get_formatted_card(line) for line in lines]
    cards_values = [0] * len(formatted_cards)
    index = len(formatted_cards) - 1

    for card in formatted_cards[::-1]:
        card_matches, card_points = count_points(card)
        cards_values[index] = count_scratchcards(index, card_matches)
        
        total_one += card_points
        total_two += cards_values[index]
        
        index -= 1

    print("Part 1:", total_one)
    print("Part 2:", total_two)
