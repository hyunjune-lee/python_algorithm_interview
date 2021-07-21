# [0. 날짜]
# 2021.07.20(화요일)
# 문제 유형: bfs, 완전 탐색
# 걸린 시간: 브루트 포스, bfs
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 상어를 기준으로 해줘야될거 같은디?
# 거리 -1 로 해준닥도 생각.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def bfs(ay, ax, cost):
    q = [(ay, ax, cost)]
    while q:
        y, x, cost = q.pop()
        for dy, dx in [(1, 0), (-1, 0), (0, -1), (0, 1), [-1, -1], [-1, 1], [1, -1], [1, 1]]:
            my, mx = y + dy, x + dx
            next_cost = cost + 1
            if not (0 <= my < N and 0 <= mx < M):
                continue
            if board[my][mx] == 0 or board[my][mx] > next_cost:
                board[my][mx] = next_cost
                q.append((my, mx, next_cost))


def solution():
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                bfs(y, x, 1)
                # for line in board:
                #     print(line)
                # print("------")
    max_safe_dist = 0
    for line in board:
        max_safe_dist = max(max_safe_dist, max(line))
    return max_safe_dist - 1


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
print(solution())
