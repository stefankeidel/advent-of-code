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

example_folds = """fold along y=7
fold along x=5
"""

def main():
    with open('dots.txt') as f:
        with open('folds.txt') as z:
            dimx, dimy, dots, folds = read_input(f.read(), z.read())
    ori = np.zeros((dimy+1, dimx+1), dtype=int)

    for (x, y) in dots:
        ori[y, x] = 1

    for (dim, fold) in folds:
        if dim == 'y':
            ori_upper = ori[0:fold, 0:ori.shape[1]]
            ori_lower = ori[fold+1:ori.shape[0], 0:ori.shape[1]]
            ori_upper = np.flipud(ori_upper)

            if ori_upper.shape[0] > ori_lower.shape[0]:
                ori_lower = np.concatenate((ori_lower, np.zeros((1,ori_upper.shape[1]))))
            ori = ori_lower + ori_upper
            ori = np.flipud(ori)
        elif dim == 'x':
            ori_left = ori[0:ori.shape[0], 0:fold]
            ori_right = ori[0:ori.shape[0], fold + 1:ori.shape[1]]

            ori_left = np.fliplr(ori_left)
            ori = ori_left + ori_right

    nz = np.fliplr((ori > 0).astype(int))
    print(np.count_nonzero(ori))
    print(np.nonzero(ori))

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

    fs = [x for x in folds.splitlines()]
    ret_folds = []
    for f in fs:
        (fold_along, coord) = f.split('=')

        ret_folds.append((fold_along[-1], int(coord)))

    return max_x, max_y, pairs, ret_folds



if __name__ == "__main__":
    main()
