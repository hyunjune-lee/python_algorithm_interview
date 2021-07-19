# [0. 날짜]
# 2021.07.19(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]

# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

# [state]
# 0: "row"
# 1: "col"
# 2: "diagonal"


def dfs(y, x, state):
    if y == N - 1 and x == N - 1:
        return 1
    res = 0
    if state == 0:
        move_list = [(0, 1, 0), (1, 1, 2)]
    elif state == 1:
        move_list = [(1, 0, 1), (1, 1, 2)]
    elif state == 2:
        move_list = [(0, 1, 0), (1, 0, 1), (1, 1, 2)]
    for dy, dx, next_state in move_list:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 1:  # 벽이라면
            continue
        if next_state == 2:
            if board[y + 1][x] == 1 or board[y][x + 1] == 1:
                continue
        res += dfs(ny, nx, next_state)
    return res


def solution():
    return dfs(0, 1, 0)


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

print(solution())
