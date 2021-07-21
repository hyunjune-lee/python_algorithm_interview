# [0. 날짜]
# 2021.07.21(수요일)
# 문제 유형: bfs
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 지금까지 추적한 내용들을 누적해서 넘겼더니 메모리 초과.. 이런거 좀 잘 생각하자

from collections import deque


def bfs(start_point):
    q = deque([start_point])
    time_board[start_point] = 0
    while q:
        cur_point = q.popleft()
        if cur_point == K:
            break
        for next_point in [cur_point - 1, cur_point + 1, cur_point * 2]:
            if not (0 <= next_point < max_size) or checked[next_point]:
                continue
            checked[next_point] = True
            time_board[next_point] = time_board[cur_point] + 1
            track_board[next_point] = cur_point
            q.append(next_point)

    track_idx = K
    q = deque([K])
    while track_idx != N:
        q.appendleft(track_board[track_idx])
        track_idx = track_board[track_idx]

    print(time_board[K])
    print(" ".join(map(str, q)))


N, K = map(int, input().split())
max_size = 100001
checked = [False] * max_size
time_board = [-1] * max_size
track_board = [-1 for _ in range(max_size)]

bfs(N)
