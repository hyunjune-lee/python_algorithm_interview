# [0. 날짜]
# 2021.07.19(월요일)
# 문제 유형: bfs
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 조건들을 최적으로 해야지 통과할 수 있어서 까다로웠다.
# [3. +개선 사항]
#  if not (0 <= my < N and 0 <= mx < M) 조건일 때 continue해줬는데.. break해줘야된다.
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# board[my][mx] <= board[y][x] + 1 일때 continue를 해줘야 하는데 break 해줘서 틀렸다.
# heap으로 해서 97%에서 틀림..
# bfs로 해야됨, dfs로 높은 값들이 추가되어서 어차피 최소로 채워넣어야됨..
# board[my][mx] <= board[y][x] + 1 조건을 board[my][mx] < board[y][x] + 1일때는 break하도록 분할해줌..
# elif board[my][mx] == board[y][x] + 1 일때는 continue 그대로 하도록
from collections import deque


def solution(board, N, M, K, start_y, start_x, end_y, end_x):
    board[start_y][start_x] = 0
    q = deque([(start_y, start_x)])
    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for mul in range(1, K + 1):
                my, mx = y + dy * mul, x + dx * mul
                next_cost = board[y][x] + 1
                if not (0 <= my < N and 0 <= mx < M) or board[my][mx] == "#" or board[my][mx] < next_cost:
                    break
                elif board[my][mx] == next_cost:
                    continue
                else:
                    board[my][mx] = next_cost
                    if my == end_y and mx == end_x:
                        return board[my][mx]
                    q.append((my, mx))
    return -1


N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append([float("inf") if x == "." else x for x in input()])
start_y, start_x, end_y, end_x = map(int, input().split())
print(solution(board, N, M, K, start_y - 1, start_x - 1, end_y - 1, end_x - 1))
