import numpy as np

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

score_complete = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def main():
    with open('input.txt') as f:
        input = read_input(f.read())

    reverse_map = {v: k for k, v in map.items()}

    autocomplete_scores = []
    for line in input:
        stack = []
        corrupted = False
        for c in line:
            if c in map.keys():
                d = stack.pop()
                if map[c] != d:
                    # discard corrupted
                    corrupted = True
                    break
            else:
                stack.append(c)

        # we're done parsing but still have stuff on the stack
        if len(stack) > 0 and not corrupted:
            autocomplete_score = 0
            while len(stack) > 0:
                c = stack.pop()
                autocomplete_score *= 5
                autocomplete_score += score_complete[reverse_map[c]]

            autocomplete_scores.append(autocomplete_score)

    print(np.median(np.sort(autocomplete_scores)))



def read_input(input=example_input):
    return input.splitlines()


if __name__ == "__main__":
    main()
