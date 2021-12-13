import numpy as np

example_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0
"""

example_folds = """
fold along y=7
fold along x=5
"""

def main():
    dimx, dimy, dots, folds = read_input()
    ori = np.zeros((dimy+1, dimx+1), dtype=int)

    for (x, y) in dots:
        ori[y, x] = 1

    pass



def read_input(input=example_input, folds=example_folds):
    lines = [x for x in input.splitlines()]

    max_x = 0
    max_y = 0
    pairs = []
    for pair in lines:
        (x, y) = pair.split(',')

        max_x = max(int(x), max_x)
        max_y = max(int(y), max_y)

        pairs.append((int(x), int(y)))

    folds = []

    return max_x, max_y, pairs, folds



if __name__ == "__main__":
    main()
