# [0. 날짜]
# 2021.07.20(화요일)
# 문제 유형: bfs, dfs
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# vistied 개념으로 탐색한 보드는 다르게 바꿔주는거 빠뜨림


def dfs(y, x, team):
    if board[y][x] != team:
        return 0
    board[y][x] = "C"
    res = 1
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        my, mx = y + dy, x + dx
        if not (0 <= my < M and 0 <= mx < N):
            continue
        res += dfs(my, mx, team)
    return res


def solution():
    W_power = 0
    B_power = 0
    for y in range(M):
        for x in range(N):
            if board[y][x] == "W":
                W_power += dfs(y, x, "W") ** 2
            elif board[y][x] == "B":
                B_power += dfs(y, x, "B") ** 2
    return W_power, B_power


N, M = map(int, input().split())
board = []
for _ in range(M):
    board.append(list(input()))
print(" ".join(map(str, solution())))
