FILE = 'input.txt'


def find_elf_with_most(filename):
    with open(filename) as f:
        highest = 0
        total = 0
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                highest = max(highest, total)
                total = 0
            else:
                total += int(line)
        print(f"Highest: {highest}")


def find_top_3_with_most(filename):
    all_totals = []
    with open(filename) as f:
        total = 0
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                all_totals.append(total)
                total = 0
            else:
                total += int(line)
    top3 = sum(sorted(all_totals)[-3:])
    print(f"Top 3 total: {top3}")


if __name__ == '__main__':
    find_elf_with_most(FILE)
    find_top_3_with_most(FILE)
