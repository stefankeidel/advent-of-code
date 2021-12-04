import re

def main():
    nums = get_drawn_numbers()
    boards = get_boards()

    while len(nums) > 0:
        drawn_num = nums.pop(0)

        # mark new num
        boards = [
            [
                [(x, True if x == drawn_num else t) for (x, t) in row]
                for row in board
            ]
            for board in boards
        ]

        # check win
        for board in boards:
            for i in range(len(board)):
                win_row = all([board[i][j][1] for j in range(len(board))])
                win_col = all(board[j][i][1] == True for j in range(len(board)))

                if win_row or win_col:
                    sum_unmarked = sum(sum([[n for (n, t) in row if t == False] for row in board], []))
                    print(sum_unmarked * drawn_num)
                    exit(0)


def get_boards():
    with open('boards.txt') as f:
        # list comprehension party
        return [
            [[(int(n), False) for n in re.split('\s+', l.strip())] for l in b.split('\n') if len(l) > 0]
            for b in f.read().split('\n\n')
        ]

def get_drawn_numbers():
    with open('drawn_numbers.txt') as f:
        return [int(x) for x in f.read().split(',')]


if __name__ == "__main__":
    main()
