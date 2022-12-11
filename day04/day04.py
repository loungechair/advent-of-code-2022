from dataclasses import dataclass
from typing import Tuple, Generator

FILE = "input.txt"

@dataclass
class Range:
    start: int
    end: int

    def contains(self, r2: "Range") -> bool:
        """Does this range contain r2?"""
        return self.start <= r2.start and r2.end <= self.end

    def overlap(self, r2: "Range") -> bool:
        return self.start <= r2.end and r2.start <= self.end

def input_generator(filename: str) -> Generator[Tuple[Range], None, None]:
    with open(filename) as f:
        for line in f:
            line = line.strip()
            first, second = line.split(",")
            f1, f2 = [int(x) for x in first.split("-")]
            s1, s2 = [int(x) for x in second.split("-")]

            yield Range(f1, f2), Range(s1, s2)


def solve(filename: str) -> Tuple[int, int]:
    num_contained = 0
    num_overlaps = 0
    for r1, r2 in input_generator(filename):
        if r1.contains(r2) or r2.contains(r1):
            num_contained += 1
        if r1.overlap(r2):
            num_overlaps += 1
    return num_contained, num_overlaps


if __name__ == '__main__':
    num_contained, num_overlaps = solve(FILE)
    print(f"Num fully contained: {num_contained}")
    print(f"Num overlaps: {num_overlaps}")