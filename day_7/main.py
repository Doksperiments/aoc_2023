
from collections import Counter

cards_list: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class CardType:
    FIVE_KIND = 7
    FOUR_KIND = 6
    FULL_HOUSE = 5
    THREE_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

def split_values(line: str) -> tuple[str, int]:

    line = line.replace('\n', '') 
    return (line.split(" ")[0], int(line.split(" ")[1]))


def get_type(hand: str) -> int:

    frequency_table: list[tuple[str, int]] = Counter(hand).most_common()

    match(frequency_table[0][1]):
        case 5:
            return CardType.FIVE_KIND
        case 4:
            return CardType.FOUR_KIND
        case 3:
            if frequency_table[1][1] == 2:
                return CardType.FULL_HOUSE
            else:
                return CardType.THREE_KIND
        case 2:
            if frequency_table[1][1] == 2:
                return CardType.TWO_PAIRS
            else:
                return CardType.ONE_PAIR
        case 1:
            return CardType.HIGH_CARD
        case _:
            raise ValueError


def get_type_joker(hand: str) -> int:

    frequency_table: list[tuple[str, int]] = Counter(hand).most_common()

    match(frequency_table[0][1]):
        case 5:
            return CardType.FIVE_KIND
        case 4:
            if frequency_table[1][0] == 'J' or frequency_table[0][0] == 'J':
                return CardType.FIVE_KIND
            return CardType.FOUR_KIND
        case 3:
            if frequency_table[1][1] == 2:
                if frequency_table[1][0] == 'J' or frequency_table[0][0] == 'J':
                    return CardType.FIVE_KIND
                return CardType.FULL_HOUSE
            elif frequency_table[0][0] == 'J' or frequency_table[1][0] == 'J' or frequency_table[2][0] == 'J':
                return CardType.FOUR_KIND
            else:
                return CardType.THREE_KIND
        case 2:
            if frequency_table[1][1] == 2:
                if frequency_table[0][0] == 'J' or frequency_table[1][0] == 'J':
                    return CardType.FOUR_KIND
                elif frequency_table[2][0] == 'J':
                    return CardType.FULL_HOUSE
                return CardType.TWO_PAIRS
            elif frequency_table[0][0] == 'J' or frequency_table[1][0] == 'J' or frequency_table[2][0] == 'J' or frequency_table[3][0] == 'J':
                return CardType.THREE_KIND
            return CardType.ONE_PAIR
        case 1:
            if frequency_table[0][0] == 'J' or frequency_table[1][0] == 'J' or frequency_table[2][0] == 'J' or frequency_table[3][0] == 'J' or frequency_table[4][0] == 'J':
                return CardType.ONE_PAIR
            return CardType.HIGH_CARD
        case _:
            raise ValueError


def get_sorted_ranking(hands: list[str], bids: list[int], joker: bool = False) -> list[list[int]]:

    sorted_lines: list[list[int]] = []
    card_to_points: dict[str, int] = {card: (i+2) for i, card in enumerate(cards_list)}
    
    if joker:
        card_to_points['J'] = 1
    
    for hand, bid in zip(hands, bids):
        sorted_lines.append([
            get_type_joker(hand) if joker else get_type(hand),  # Hand type
            bid,                                                # Bid amount for hand
            *[card_to_points[card] for card in hand]            # Cards value in hand
        ])

    return sorted(sorted_lines, key= lambda line: (line[0], *line[2:]))


if __name__ == "__main__":
    lines: list[str]
    cards: list[str] = []
    bids: list[int] = []
    updated_bids: list[int]
    updated_bids_joker: list[int]

    with open("day_7/input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        card, bid = split_values(line)
        cards.append(card)
        bids.append(bid)

    updated_bids = [hand[1]*(i+1) for i, hand in enumerate(get_sorted_ranking(cards, bids))]
    updated_bids_joker = [hand[1]*(i+1) for i, hand in enumerate(get_sorted_ranking(cards, bids, joker=True))]

    print("Part 1:", sum(updated_bids))
    print("Part 2:", sum(updated_bids_joker))
