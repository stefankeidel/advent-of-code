example_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

map = {
    '>': '<',
    '}': '{',
    ')': '(',
    ']': '[',
}

score_illegal = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def main():
    with open('input.txt') as f:
        input = read_input(f.read())
    score = 0

    for line in input:
        stack = []
        for c in line:
            if c in map.keys():
                d = stack.pop()
                if map[c] != d:
                    print(f"Expected {d} but found {c} instead.")
                    score += score_illegal[c]
                    continue
            else:
                stack.append(c)
    print(score)


def read_input(input=example_input):
    return input.splitlines()


if __name__ == "__main__":
    main()
