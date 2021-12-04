from functools import reduce


def main():
    i = [list(x) for x in get_input()]

    # we still need this, no?
    z = reduce(bin_dim_sum, i)
    gamma_rate = [0 if int(x) < len(i)/2 else 1 for x in z]

    oxy = i

    j = 0
    while j < len(gamma_rate):
        oxy = [x for x in oxy if int(x[j]) == gamma_rate[j]]
        z = reduce(bin_dim_sum, oxy)
        gamma_rate = [0 if int(x) < len(oxy)/2 else 1 for x in z]
        if len(oxy) == 1:
            break
        j+=1

    int_oxy = int("".join(str(i) for i in oxy[0]), 2)


    # terrible copy+paste
    z = reduce(bin_dim_sum, i)
    gamma_rate = [1 if int(x) < len(i)/2 else 0 for x in z]

    oxy = i

    j = 0
    while j < len(gamma_rate):
        oxy = [x for x in oxy if int(x[j]) == gamma_rate[j]]
        z = reduce(bin_dim_sum, oxy)
        gamma_rate = [1 if int(x) < len(oxy)/2 else 0 for x in z]
        if len(oxy) == 1:
            break
        j+=1

    int_co2 = int("".join(str(i) for i in oxy[0]), 2)

    print(int_oxy * int_co2)


def bin_dim_sum(x, y):
    return [str(int(a) + int(b)) for a, b in zip(x, y)]


def get_input():
    with open('input.txt') as f:
        return f.read().splitlines()

if __name__ == "__main__":
    main()
