import numpy as np

example_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

def main():
    with open('input.txt') as f:
        input = read_input(f.read())
    input = np.array(input)
    ones = np.ones((input.shape[0], input.shape[1]), dtype=int)

    i = 0
    
    while True:
        blinked_this_turn = 0

        input = input + ones

        blinkers = np.where(input > 9)

        while len(blinkers[0]) > 0:
            blinked_this_turn += len(blinkers[0])

            for c,v in enumerate(blinkers[0]):
                # reset blinked octopus
                input[blinkers[0][c], blinkers[1][c]] = -1

                # increment the surrounders
                for x in range(blinkers[0][c]-1, blinkers[0][c]+2):
                    for y in range(blinkers[1][c]-1, blinkers[1][c]+2):
                        if x < 0 or y < 0:
                            continue
                        try:
                            if input[x][y] != -1:
                                input[x][y] += 1
                        except IndexError:
                            pass

            # check for new blinkers
            blinkers = np.where(input > 9)

        # once no more blinkers, exist, we reset
        input[input == -1] = 0
        i += 1

        if blinked_this_turn == (input.shape[0] * input.shape[1]):
            print(f"all blinked on turn {i}")
            break



def read_input(input=example_input):
    d2 = [[int(y) for y in x] for x in input.splitlines()]
    return d2


if __name__ == "__main__":
    main()
