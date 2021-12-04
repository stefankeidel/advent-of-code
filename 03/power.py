from functools import reduce


def main():
    i = [list(x) for x in get_input()]
    z = reduce(bin_dim_sum, i)
    gamma_rate = [0 if int(x) < len(i)/2 else 1 for x in z]
    int_gamma_rate = int("".join(str(i) for i in gamma_rate), 2)
    int_epsilon_rate = int("".join(str(1 if i == 0 else 0) for i in gamma_rate), 2)

    print(int_gamma_rate * int_epsilon_rate)


def bin_dim_sum(x, y):
    return [str(int(a) + int(b)) for a, b in zip(x, y)]


def get_input():
    with open('input.txt') as f:
        return f.read().splitlines()

if __name__ == "__main__":
    main()
