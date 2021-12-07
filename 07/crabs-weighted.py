import numpy as np


def main():
    crabs = parse_list()
    average = np.average(crabs)
    pick_fl = np.floor(average)
    pick_cl = np.ceil(average)
    calc_fl = [(n*(n+1))/2 for n in np.abs(crabs - pick_fl)]
    calc_cl = [(n * (n + 1)) / 2 for n in np.abs(crabs - pick_cl)]
    print(np.min([np.sum(calc_fl), np.sum(calc_cl)]))


def parse_list():
    with open('input.txt') as f:
        return np.array([int(x.strip()) for x in f.read().split(',')])

if __name__ == "__main__":
    main()
