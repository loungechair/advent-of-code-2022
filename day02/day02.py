from enum import Enum

FILE = "input.txt"


class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Outcome(Enum):
    Lose = 'X'
    Draw = 'Y'
    Win = 'Z'


beats = {
    RPS.Rock: RPS.Scissors,
    RPS.Paper: RPS.Rock,
    RPS.Scissors: RPS.Paper
}


def p1_lookup(v):
    return RPS(1 + ord(v) - ord('A'))


def p2_lookup(v):
    return RPS(1 + ord(v) - ord('X'))


def score_rps_part(p1, p2):
    """
    Determines if p2 beats p1
    """
    if p1 == p2:
        return 3  # draw
    if p1 == beats[p2]:
        return 6
    else:
        return 0


def score_game(p1, p2):
    return p2.value + score_rps_part(p1, p2)


def pairs_generator(filename):
    with open(filename) as f:
        for line in f:
            p1, p2 = line.split()
            yield p1, p2


def get_total_score(filename):
    sum = 0
    for p1, p2 in pairs_generator(filename):
        p1 = p1_lookup(p1)
        p2 = p2_lookup(p2)
        sum += score_game(p1, p2)

    return sum


def find_right_shape(p1, outcome):
    if outcome == Outcome.Draw:
        return p1
    elif outcome == Outcome.Lose:
        return beats[p1]
    else:
        return beats[beats[p1]]


def play_second_game(filename):
    total_score = 0
    for p1, outcome in pairs_generator(filename):
        p1 = p1_lookup(p1)
        p2 = find_right_shape(p1, Outcome(outcome))
        total_score += score_game(p1, p2)
    return total_score


if __name__ == '__main__':
    print(f"Total score: {get_total_score(FILE)}")
    print(f"Total game2: {play_second_game(FILE)}")