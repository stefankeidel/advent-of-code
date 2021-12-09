import functools
import numpy as np
from scipy.ndimage import label, generate_binary_structure
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion

example_input = """2199943210
3987894921
9856789892
8767896789
9899965678
"""

def safe_get(l, i, j):
    if i < 0 or j < 0:
        return None
    try:
        return l[i][j]
    except IndexError:
        return None

def is_local_minimum(i,j,input):
    val = input[i][j]
    neighbors = []
    labeled_array, num_features = label(input)

    neighbors.append(safe_get(input, i-1, j))
    neighbors.append(safe_get(input, i+1, j))
    neighbors.append(safe_get(input, i, j-1))
    neighbors.append(safe_get(input, i, j+1))
    neighbors = np.array([x for x in neighbors if x is not None])

    return np.all(neighbors > val)

def main():
    with open('input.txt') as f:
        input = read_input(f.read())

    minima = []
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if is_local_minimum(i,j,input):
                minima.append(input[i][j])

    print(sum([x+1 for x in minima]))
    input = DFS(4,4,input)
    i = -1


def DFS(x, y, input):
    input[x][y] = None
    for dx in range(x-1, x):
        for dy in range(y-1, y):
            if safe_get(input, dx, dy) is not None:
                return DFS(dx, dy, input)
    return input



def read_input(input=example_input):
    d2 = [[int(y) for y in x] for x in input.splitlines()]
    return d2


if __name__ == "__main__":
    main()
