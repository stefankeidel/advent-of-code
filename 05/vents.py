import re

def main():
    with open('input.txt') as f:
        lines = [x for x in f.read().splitlines()]

        final = {}
        for line in lines:
            (x1, y1, x2, y2) = [int(x) for x in re.split('[^0-9]+', line)]

            if y1 == y2:  # horizontal line
                f = min(x1, x2)
                t = max(x1, x2)
                for i in range(f, t+1):
                    try:
                        final[i, y1] += 1
                    except KeyError:
                        final[i, y1] = 1
            if x1 == x2:  # vertical line
                f = min(y1, y2)
                t = max(y1, y2)
                for i in range(f, t+1):
                    try:
                        final[x1, i] += 1
                    except KeyError:
                        final[x1, i] = 1

        print(len([x for x in final.values() if x >= 2]))


if __name__ == "__main__":
    main()
