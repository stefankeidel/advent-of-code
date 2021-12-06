import numpy as np
import pandas as pd
import cProfile

def main():
    fish = parse_list()

    counts = {}
    freq = np.asarray(np.unique(fish, return_counts=True)).T
    for f in freq:
        counts[f[0]] = f[1]

    for d in range(256):
        counts = sim_day(counts)
        print(f"{d+1}: {sum(counts.values())}")

    print(sum(counts.values()))


def sim_day(fish_counts):
    new_counts = {}
    for i in range(-1, 9):
        new_counts[i] = 0

    for c in fish_counts:
        if c >= 0:
            new_counts[c-1] = fish_counts[c]

    new_counts[6] += new_counts[-1]
    new_counts[8] += new_counts[-1]
    new_counts[-1] = 0
    return new_counts



def parse_list():
    with open('input.txt') as f:
        return [int(x.strip()) for x in f.read().split(',')]


if __name__ == "__main__":
    #cProfile.run('main()')
    main()
