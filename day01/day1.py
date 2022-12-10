import heapq

FILE = 'input.txt'


def totals_generator(filename):
    with open(filename) as f:
        total = 0
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                yield total
                total = 0
            else:
                total += int(line)


def find_elf_with_most(filename):
    highest = 0
    for total in totals_generator(filename):
        highest = max(highest, total)
    print(f"Highest: {highest}")


def find_top_3_with_most(filename):
    all_totals = []
    for total in totals_generator(filename):
        heapq.heappush(all_totals, total)
    top3 = sum(heapq.nlargest(3, all_totals))
    print(f"Top 3 total: {top3}")


if __name__ == '__main__':
    find_elf_with_most(FILE)
    find_top_3_with_most(FILE)
