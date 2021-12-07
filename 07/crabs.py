import numpy as np

def main():
    crabs = parse_list()
    target = np.median(crabs)
    print(np.sum(np.abs(crabs - target)))


def parse_list():
    with open('input.txt') as f:
        return np.array([int(x.strip()) for x in f.read().split(',')])


if __name__ == "__main__":
    #cProfile.run('main()')
    main()
