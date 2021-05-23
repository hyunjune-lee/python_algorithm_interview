def check_x(ret, y, x):
    for row in range(y):
        if ret[row] == x or abs(x - ret[row]) == y - row:
            return False
    return True


def n_queens(n, y, queen_pos):
    if y == n:
        return queen_pos[:]

    for x in range(n):
        if check_x(queen_pos, y, x):
            queen_pos[y] = x
            res = n_queens(n, y + 1, queen_pos)
            if res:
                return res
            queen_pos[y] = -1

    return None


T = int(input())
for _ in range(T):
    n = int(input())
    queen_pos = n_queens(n, 0, [-1 for _ in range(n)])
