import functools
from enum import Enum
from typing import Tuple

FILE = "input.txt"


class RPS(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2


class Outcome(Enum):
    Lose = 'X'
    Draw = 'Y'
    Win = 'Z'


def what_beats(shape: RPS) -> RPS:
    return RPS((shape.value + 1) % 3)


def what_loses_to(shape: RPS) -> RPS:
    return RPS((shape.value + 2) % 3)


def lookup(v: str, offset: str) -> RPS:
    return RPS(ord(v) - ord(offset))


p1_lookup = functools.partial(lookup, offset='A')
p2_lookup = functools.partial(lookup, offset='X')


def score_rps_part(p1: RPS, p2: RPS) -> int:
    """
    Determines if p2 beats p1
    """
    if p1 == p2:
        return 3
    elif p2 == what_beats(p1):
        return 6
    else:
        return 0


def score_game(p1: RPS, p2: RPS) -> int:
    return 1 + p2.value + score_rps_part(p1, p2)


def pairs_generator(filename: str) -> Tuple[str, str]:
    with open(filename) as f:
        for line in f:
            p1, p2 = line.split()
            yield p1, p2


def get_total_score(filename: str) -> int:
    total_score = 0
    for p1, p2 in pairs_generator(filename):
        p1 = p1_lookup(p1)
        p2 = p2_lookup(p2)
        total_score += score_game(p1, p2)
    return total_score


def find_right_shape(p1: RPS, outcome: Outcome) -> RPS:
    if outcome == Outcome.Draw:
        return p1
    elif outcome == Outcome.Lose:
        return what_loses_to(p1)
    else:
        return what_beats(p1)


def play_second_game(filename: str) -> int:
    total_score = 0
    for p1, outcome in pairs_generator(filename):
        p1 = p1_lookup(p1)
        p2 = find_right_shape(p1, Outcome(outcome))
        total_score += score_game(p1, p2)
    return total_score


if __name__ == '__main__':
    print(f"Total score: {get_total_score(FILE)}")
    print(f"Total game2: {play_second_game(FILE)}")