import re
import numpy as np


def main():
    signals = parse_list()
    results = []

    for signal in signals:
        one = four = seven = set()
        list235 = []
        for letters in signal[0].split(" "):
            # collect possible letters
            if len(letters) == 2:  # 1
                one = set(letters)
            if len(letters) == 4:  # 4
                four = set(letters)
            if len(letters) == 3:  # 7
                seven = set(letters)
            if len(letters) == 5:  # 2, 3, 5
                list235.append(set(letters))

        common235 = list235[0] & list235[1] & list235[2]

        guesswork = {
            "top": (seven - one) & common235,
            "top-left": four - seven - one,
            "top-right": four & seven & one,
            "center": (four - seven - one) & common235,
            "bottom-left": set("abcdefg") - four - seven - one,
            "bottom-right": four & seven & one,
            "bottom": (set("abcdefg") - four - seven - one) & common235,
        }

        letters_taken = set()
        for i in guesswork:
            if len(guesswork[i]) == 1:
                letters_taken = letters_taken.union(guesswork[i])

        for i in guesswork:
            if len(guesswork[i]) > 1:
                guesswork[i] = guesswork[i] - letters_taken

        # now might need to decide between 5 and 2 to resolve bottom-right and top-right
        two_five = [x for x in list235 if not one.issubset(x)]

        five = (
            two_five[0] if guesswork["top-left"].issubset(two_five[0]) else two_five[1]
        )
        two = (
            two_five[0] if guesswork["bottom-left"].issubset(two_five[0]) else two_five[1]
        )

        if five == two:
            raise Exception()

        guesswork["top-right"] = guesswork["top-right"] & two
        guesswork["bottom-right"] = guesswork["bottom-right"] - guesswork["top-right"]

        for i in guesswork:
            if len(guesswork[i]) > 1:
                raise Exception()

        result = []
        for letters in signal[1].split(" "):
            check = set(letters)

            if check == guesswork["top"] \
                    .union(guesswork["top-right"]) \
                    .union(guesswork["top-left"]) \
                    .union(guesswork["bottom-right"]) \
                    .union(guesswork["bottom-left"]) \
                    .union(guesswork["bottom"]):
                result.append(0)

            if check == guesswork["top-right"] \
                    .union(guesswork["bottom-right"]):
                result.append(1)

            if check == guesswork["top"] \
                    .union(guesswork["top-right"]) \
                    .union(guesswork["center"]) \
                    .union(guesswork["bottom-left"]) \
                    .union(guesswork["bottom"]):
                result.append(2)

            if check == guesswork["top"] \
                    .union(guesswork["top-right"]) \
                    .union(guesswork["center"]) \
                    .union(guesswork["bottom-right"]) \
                    .union(guesswork["bottom"]):
                result.append(3)

            if check == guesswork["top-left"] \
                    .union(guesswork["top-right"]) \
                    .union(guesswork["center"]) \
                    .union(guesswork["bottom-right"]):
                result.append(4)

            if check == guesswork["top"] \
                    .union(guesswork["top-left"]) \
                    .union(guesswork["center"]) \
                    .union(guesswork["bottom-right"]) \
                    .union(guesswork["bottom"]):
                result.append(5)

            if check == guesswork["top"] \
                    .union(guesswork["top-left"]) \
                    .union(guesswork["center"]) \
                    .union(guesswork["bottom-left"]) \
                    .union(guesswork["bottom-right"]) \
                    .union(guesswork["bottom"]):
                result.append(6)

            if check == guesswork["top"] \
                    .union(guesswork["top-right"]) \
                    .union(guesswork["bottom-right"]):
                result.append(7)

            if len(check) == 7:
                result.append(8)

            if check == guesswork["top"] \
                    .union(guesswork["top-left"]) \
                    .union(guesswork["top-right"]) \
                    .union(guesswork["center"]) \
                    .union(guesswork["bottom-right"]) \
                    .union(guesswork["bottom"]):
                result.append(9)

        if len(result) != 4:
            raise Exception()

        results.append(int(''.join(map(str, result))))

    print(sum(results))


def parse_list():
    with open("input.txt") as f:
        l = [x for x in f.read().splitlines()]
        ret = []
        for line in l:
            s = line.split("|")
            ret.append((s[0].strip(), s[1].strip()))

    return ret


if __name__ == "__main__":
    main()
