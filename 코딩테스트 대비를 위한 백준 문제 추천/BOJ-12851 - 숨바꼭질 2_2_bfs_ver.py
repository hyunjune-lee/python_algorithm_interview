# [0. 날짜]
# 2021.07.20(화요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 가장 빠른 이니깐 bfs로 해서 한 주기에 체크하는 방법의 개수
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
# 그냥 q만 쓸때는 2964ms, next_q랑 같이 쓰니깐 1216ms이다.
#  => q가 너무 길어져서 pop(0) 성능이 끔찍해진 결과인듯
# next_q랑 deque로 쓰니 212ms
# 그냥 q하고 deque 쓰니 216ms
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# N < K일때는 그냥 그 차이 만큼, 그리고 가지수는 1만큼 출력하고 return을 안해줘서 bfs도 돌았다..
from collections import deque


def bfs(start_point):
    q = deque([(start_point, 0)])
    method_count = 1
    while q:
        cur_point, time = q.popleft()
        dp_board[cur_point] = time
        if cur_point == K:
            break
        for next_point in [cur_point - 1, cur_point + 1, 2 * cur_point]:
            if not (0 <= next_point <= 100000):
                continue
            next_time = time + 1
            if dp_board[next_point] < next_time:
                continue
            dp_board[next_point] = next_time
            q.append((next_point, next_time))
    while q:
        cur_point, time = q.popleft()
        if cur_point == K and dp_board[K] == time:
            method_count += 1
    print(dp_board[K])
    print(method_count)


def solution():
    if K <= N:
        print(N - K)
        print(1)
        return
    bfs(N)


N, K = map(int, input().split())
dp_board = [float("inf") for _ in range(100001)]
solution()
