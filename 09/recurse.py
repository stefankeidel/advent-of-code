import numpy as np

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
                minima.append((i,j))

    collections = []
    for (i,j) in minima:
        collection = DFS(i, j, input, [(i,j)])
        collections.append(len(collection))

    print(np.product(list(reversed(np.sort(collections)))[0:3]))



def DFS(x, y, input, collection):
    input[x][y] = None

    check = [
        (x, y - 1),
        (x, y + 1),
        (x + 1, y),
        (x - 1, y),
    ]

    for (dx, dy) in check:
        val = safe_get(input, dx, dy)
        if val is not None and val != 9:
            collection.append((dx, dy))
            collection = DFS(dx, dy, input, collection)
    return collection



def read_input(input=example_input):
    d2 = [[int(y) for y in x] for x in input.splitlines()]
    return d2


if __name__ == "__main__":
    main()
