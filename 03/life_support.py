from functools import reduce
import operator


def main():
    i = [list(x) for x in get_input()]
    int_oxy = compute_life_support(i, operator.lt)
    int_co2 = compute_life_support(i, operator.ge)

    print(int_oxy * int_co2)


def compute_life_support(input_list, comp_fn):
    num_list = input_list

    j = 0
    while True:
        z = reduce(bin_dim_sum, num_list)
        gamma_rate = [0 if comp_fn(int(x), len(num_list) / 2) else 1 for x in z]
        num_list = [x for x in num_list if int(x[j]) == gamma_rate[j]]

        if len(num_list) == 1:
            break

        j += 1
        if j == len(gamma_rate):
            break

    return int("".join(str(i) for i in num_list[0]), 2)



def bin_dim_sum(x, y):
    return [str(int(a) + int(b)) for a, b in zip(x, y)]


def get_input():
    with open('test_input.txt') as f:
        return f.read().splitlines()

if __name__ == "__main__":
    main()
