# [0. 날짜]
# 2021.07.19(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# board[my][mx] <= board[y][x] + 1 일때 continue를 해줘야 하는데 break 해줘서 틀렸다.

import heapq


def solution(board, N, M, K, start_y, start_x, end_y, end_x):
    q = [(0, start_y, start_x)]
    while q:
        cost, y, x = heapq.heappop(q)
        print(y, x)
        board[y][x] = cost
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            for mul in range(1, K + 1):
                my, mx = y + dy * mul, x + dx * mul
                if not (0 <= my < N and 0 <= mx < M):
                    continue
                elif board[my][mx] == "#" or board[my][mx] < cost + 1:
                    break
                elif board[my][mx] == cost + 1:
                    continue
                else:
                    board[my][mx] = cost + 1
                    if my == end_y and mx == end_x:
                        return cost + 1
                    heapq.heappush(q, (cost + 1, my, mx))
        for l in board:
            print(l)
        print("---")
    return -1


N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append([float("inf") if x == "." else x for x in input()])
start_y, start_x, end_y, end_x = map(int, input().split())
print(solution(board, N, M, K, start_y - 1, start_x - 1, end_y - 1, end_x - 1))
