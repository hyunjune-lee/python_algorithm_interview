def check_x(queen_pos, y, x):
    for row in range(y):
        if queen_pos[row] == x or abs(x - queen_pos[row]) == y - row:
            return False
    return True


def n_queens(n, y, board, queen_pos):
    if y == n:
        for line in board:
            print("".join(map(str, line)))
        return True

    exist_answer = False
    for x in range(n):
        if check_x(queen_pos, y, x):
            board[y][x] = "Q"
            queen_pos[y] = x
            ret = n_queens(n, y + 1, board, queen_pos)
            if ret:
                exist_answer = True
            board[y][x] = "X"

    return exist_answer


T = int(input())
for _ in range(T):
    n = int(input())
    board = [["X" for _ in range(n)] for _ in range(n)]
    queen_pos = [-1 for _ in range(n)]
    if not n_queens(n, 0, board, queen_pos):
        print()
