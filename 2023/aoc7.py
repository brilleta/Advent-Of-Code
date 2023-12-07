import enum
from functools import cmp_to_key, total_ordering
from typing import Dict

lines = open("/home/aurelien/AOC/2023/aoc7.txt").read().splitlines()


order = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

order2 = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


@total_ordering
class HandType(enum.Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE = 3
    FULL_HOUSE = 4
    FOUR = 5
    FIVE = 6

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


def count_cards(hand: str) -> Dict[str, int]:
    hand_set = set(hand)
    count_of_cards = dict()
    for card in hand_set:
        count_of_card = 0
        for c in hand:
            if c == card:
                count_of_card += 1
        count_of_cards[card] = count_of_card
    return count_of_cards


def get_hand_type(hand: str) -> HandType:
    count_of_cards = count_cards(hand)
    if len(count_of_cards) == 1 and list(count_of_cards.values())[0] == 5:
        return HandType.FIVE
    elif len(count_of_cards) == 2:
        if set(count_of_cards.values()) == {3, 2}:
            return HandType.FULL_HOUSE
        elif set(count_of_cards.values()) == {4, 1}:
            return HandType.FOUR
    elif len(count_of_cards) == 3:
        if set(count_of_cards.values()) == {3, 1}:
            return HandType.THREE
        elif set(count_of_cards.values()) == {2, 1}:
            return HandType.TWO_PAIR
    elif len(count_of_cards) == 4:
        return HandType.ONE_PAIR
    else:
        return HandType.HIGH_CARD


def get_hand_type2(hand: str) -> HandType:
    count_of_cards = count_cards(hand)
    jokers = 0 if "J" not in count_of_cards else count_of_cards["J"]
    if len(count_of_cards) == 1 and list(count_of_cards.values())[0] == 5:
        return HandType.FIVE
    elif len(count_of_cards) == 2:
        if jokers != 0:
            return HandType.FIVE
        elif set(count_of_cards.values()) == {3, 2}:
            return HandType.FULL_HOUSE
        elif set(count_of_cards.values()) == {4, 1}:
            return HandType.FOUR
    elif len(count_of_cards) == 3:
        if set(count_of_cards.values()) == {3, 1}:
            if jokers != 0:
                return HandType.FOUR
            return HandType.THREE
        elif set(count_of_cards.values()) == {2, 1}:
            if jokers == 2:
                return HandType.FOUR
            elif jokers == 1:
                return HandType.FULL_HOUSE
            return HandType.TWO_PAIR
    elif len(count_of_cards) == 4:
        if jokers != 0:
            return HandType.THREE
        return HandType.ONE_PAIR
    else:
        if jokers != 0:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD


def second_order_compare(hand1: str, hand2: str, order: Dict[str, int]) -> int:
    if hand1 == hand2:
        return 0
    for c1, c2 in zip(hand1, hand2):
        if order[c1] < order[c2]:
            return -1
        elif order[c1] > order[c2]:
            return 1


def compare_hand(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(" ")[0]
    hand2 = hand2.split(" ")[0]
    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)
    if hand1_type < hand2_type:
        return -1
    elif hand1_type > hand2_type:
        return 1
    else:
        return second_order_compare(hand1, hand2, order)


def compare_hand2(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(" ")[0]
    hand2 = hand2.split(" ")[0]
    hand1_type = get_hand_type2(hand1)
    hand2_type = get_hand_type2(hand2)
    if hand1_type < hand2_type:
        return -1
    elif hand1_type > hand2_type:
        return 1
    else:
        return second_order_compare(hand1, hand2, order2)


def first_star(lines):
    return sum(
        (i + 1) * int(line.split(" ")[1])
        for i, line in enumerate(sorted(lines, key=cmp_to_key(compare_hand)))
    )


def second_star(lines):
    return sum(
        (i + 1) * int(line.split(" ")[1])
        for i, line in enumerate(sorted(lines, key=cmp_to_key(compare_hand2)))
    )


print(first_star(lines))
print(second_star(lines))
