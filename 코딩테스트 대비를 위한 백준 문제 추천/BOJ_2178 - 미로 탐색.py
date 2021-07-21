# [0. 날짜]
# 2021.07.20(화요일)
# 문제 유형: bfs
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# vistied 개념으로 탐색한 보드는 다르게 바꿔주는거 빠뜨림

from collections import deque


def bfs(ay, ax):
    q = deque([(ay, ax, 1)])
    while q:
        y, x, move_count = q.popleft()
        # 종결 조건
        if y == N - 1 and x == M - 1:
            return move_count
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            my, mx = y + dy, x + dx
            if not (0 <= my < N and 0 <= mx < M):
                continue
            if board[my][mx] == 0 or board[my][mx] == 2:
                continue
            # visited
            board[my][mx] = 2
            q.append((my, mx, move_count + 1))


def solution():
    return bfs(0, 0)


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, list(input()))))
print(solution())
