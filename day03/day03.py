from typing import Generator, Tuple, Set

FILE = "input.txt"

def calculate_priority(letter: str) -> int:
    if letter.islower():
        return 1 + ord(letter) - ord('a')
    else:
        return 27 + ord(letter) - ord('A')


def find_total_priority(filename: str) -> int:
    total_priority = 0
    with open(filename) as f:
        for line in f:
            items = line.strip()
            split_point = len(items)//2
            items1, items2 = items[:split_point], items[split_point:]
            misplaced = list(set(items1).intersection(set(items2)))[0]
            priority = calculate_priority(misplaced)
            total_priority += priority
    return total_priority


def group_generator(filename: str) -> Generator[Tuple[Set[str]], None, None]:
    group = []
    with open(filename) as f:
        for line in f:
            group.append(line.rstrip())
            if len(group) == 3:
                yield [set(x) for x in group]
                group = []


def find_group_priorities(filename: str) -> int:
    total_priority = 0
    for a, b, c in group_generator(filename):
        (badge, ) = a.intersection(b).intersection(c)
        priority = calculate_priority(badge)
        total_priority += calculate_priority(badge)
    return total_priority


if __name__ == '__main__':
    print(f"Total priority: {find_total_priority(FILE)}")
    print(f"Group total priority: {find_group_priorities(FILE)}")