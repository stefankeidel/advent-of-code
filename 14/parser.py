import numpy as np
import pyparsing as pp

default_template = "NNCB"

default_rules = """CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

def main():
    with open('template.txt') as f:
        with open('rules.txt') as r:
            template, rules = read_input(f.read(), r.read())

    for i in range(0, 40):
        print(i)
        left = template.pop(0)
        final = [left]
        while True:
            right = template.pop(0)

            if left + right in rules:
                final.append(rules[left + right])
                final.append(right)
            else:
                final.append(right)

            left = right

            if(len(template) == 0):
                template = final.copy()
                break

    print(len(template))
    unique, counts = np.unique(template, return_counts=True)
    print(max(counts) - min(counts))
    pass


def read_input(template=default_template, rules=default_rules):
    rls = {}
    r = [x for x in rules.splitlines()]
    for rule in r:
        s = rule.split(' -> ')
        rls[s[0]] = s[1]
    return list(template), rls


if __name__ == "__main__":
    main()