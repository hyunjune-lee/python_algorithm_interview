# [0. 날짜]
# 2021.07.21(수요일)
# 문제 유형: dfs, bfs
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)


def dfs(y, x):
    res = 1
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        my, mx = y + dy, x + dx
        if not (0 <= my < N and 0 <= mx < M):
            continue
        # 진입 조건
        if board[my][mx] == "." or board[my][mx] == "@":
            continue
        # 마스킹
        board[my][mx] = "@"
        res += dfs(my, mx)
    return res


def solution():
    max_trash_size = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == "#":
                board[y][x] = "@"
                max_trash_size = max(dfs(y, x), max_trash_size)

    return max_trash_size


N, M, K = map(int, input().split())
board = [["." for _ in range(M)] for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = "#"
print(solution())
