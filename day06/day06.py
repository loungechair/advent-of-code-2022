FILE = "input.txt"

def process_file(filename, window_size):
    with open(filename) as f:
        data = f.read().rstrip()
        for idx in range(window_size, len(data)):
            window = data[idx-window_size:idx]
            if len(set(window)) == window_size:
                return idx
    return -1


if __name__ == '__main__':
    answer = process_file(FILE, 4)
    print(answer)
    answer2 = process_file(FILE, 14)
    print(answer2)