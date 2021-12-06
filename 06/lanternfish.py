import time

def main():
    fish = parse_list()
    prev_day_pef = 1
    for d in range(256):
        start_time_perf = time.perf_counter()
        sim_day(fish)
        elapsed_time_perf = time.perf_counter() - start_time_perf
        print(f"{d+1}: {len(fish)} - elapsed: {elapsed_time_perf}. factor: {elapsed_time_perf/prev_day_pef}")
        prev_day_pef = elapsed_time_perf
    print(len(fish))


def sim_day(fish):
    i = 0
    stop = len(fish)-1 # we change the length of the array, but we don't want to touch the new stuff
    while stop >= i:
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1
        i += 1
    return fish



def parse_list():
    with open('input.txt') as f:
        return [int(x.strip()) for x in f.read().split(',')]

if __name__ == "__main__":
    main()
