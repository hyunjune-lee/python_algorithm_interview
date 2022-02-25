import sys

input = sys.stdin.readline


N, M = map(int, input().split())
board = [[0 for _ in range(N + 1)]]
for _ in range(N):
    board.append([0] + list(map(int, input().split())))

# 누적합 구하기
for y in range(1, N + 1):
    for x in range(1, N + 1):
        board[y][x] = board[y][x] + board[y - 1][x] + board[y][x - 1] - board[y - 1][x - 1]

# 구간합 구하기
for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(board[y2][x2] - board[y2][x1 - 1] - board[y1 - 1][x2] + board[y1 - 1][x1 - 1])
