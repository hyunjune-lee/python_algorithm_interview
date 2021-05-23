def check_x(board, y, x):
    for row in range(y):
        if board[row][x] == "Q" or abs(x - board[row].index("Q")) == y - row:
            return False
    return True


def n_queens(n, y, board):
    if y == n:
        for line in board:
            print("".join(map(str, line)))
        return True

    exist_answer = False
    for x in range(n):
        if check_x(board, y, x):
            board[y][x] = "Q"
            ret = n_queens(n, y + 1, board)
            if ret:
                exist_answer = True
            board[y][x] = "X"

    return exist_answer


T = int(input())
for _ in range(T):
    n = int(input())
    board = [["X" for _ in range(n)] for _ in range(n)]
    if not n_queens(
        n,
        0,
        board,
    ):
        for line in board:
            print(" " * n)
