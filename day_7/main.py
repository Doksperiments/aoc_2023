
from collections import Counter

cards: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_to_points: dict[str, int] = {card: (i+2) for i, card in enumerate(cards)}


def split_values(line: str) -> tuple[str, int]:

    line = line.replace('\n', '') 
    return (line.split(" ")[0], int(line.split(" ")[1]))


def get_type(hand: str) -> int:

    frequency_table: list[tuple[str, int]] = Counter(hand).most_common()

    match(frequency_table[0][1]):
        case 5:
            return 7        # Five of a kind
        case 4:
            return 6        # Four of a kind
        case 3:
            if frequency_table[1][1] == 2:
                return 5    # Full house
            else:
                return 4    # Three of a kind
        case 2:
            if frequency_table[1][1] == 2:
                return 3    # Two pairs
            else:
                return 2    # One pair
        case 1:
            return 1        # High card
        case _:
            raise ValueError
    

def get_sorted_ranking(hands: list[str], bids: list[int]):

    sorted_lines: list[list[int]] = []
    
    for hand, bid in zip(hands, bids):
        sorted_lines.append([
            get_type(hand),                             # Hand type
            bid,                                        # Bid amount for hand
            *[card_to_points[card] for card in hand]    # Cards value in hand
        ])

    return sorted(sorted_lines, key= lambda line: (line[0], *line[2:]))


if __name__ == "__main__":
    lines: list[str]
    cards: list[str] = []
    bids: list[int] = []
    updated_bids: list[int]

    with open("day_7/input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        card, bid = split_values(line)
        cards.append(card)
        bids.append(bid)

    updated_bids = [hand[1]*(i+1) for i, hand in enumerate(get_sorted_ranking(cards, bids))]
    
    print("Part 1:", sum(updated_bids))
