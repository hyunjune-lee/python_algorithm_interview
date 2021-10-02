# [0. 날짜]
# 2021.10.02(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]	
# 맨 처음에 0인 경우를 체크 안해줬음!!

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


def bfs():
    if N <= 0:
        return -1
    if board[0][0] == 0:
        return -1
    
    start = (0,0,0)
    q = deque([start])

    visited = [[False for _ in range(N)] for _ in range(N)]
    while q:
        y, x, dist = q.popleft()
        if y == N - 1 and x == N - 1:
            return dist
        for dy, dx in [(1,0), (-1,0), (0, 1), (0, -1)]:
            my, mx = y + dy, x + dx
            if 0 <= my < N and 0 <= mx < N:
                if not visited[my][mx] and board[my][mx] == 1:
                    visited[my][mx] = True
                    q.append((my,mx, dist + 1))
    return -1

ret = bfs()
if ret <= 2:
    print(ret)
else:
    print((ret - 3)* 3 + 5)

        

