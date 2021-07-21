# [0. 날짜]
# 2021.07.20(화요일)
# 문제 유형: bfs, 0-1 bfs, 다익스트라?
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# ...
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 인덱스 에러     while teleport_point <= K and teleport_point <= 50000:
# 0 <= 를 안해줬다..

from collections import deque


def bfs(start_point):
    q = deque([start_point])
    dist[start_point] = 0
    while q:
        cur_point = q.popleft()
        if cur_point == K:
            return dist[K]
        if cur_point * 2 < max_size and not checked[cur_point * 2]:
            q.appendleft(cur_point * 2)
            checked[cur_point * 2] = True
            dist[cur_point * 2] = dist[cur_point]
        for next_point in [cur_point - 1, cur_point + 1]:
            if not (0 <= next_point < max_size) or checked[next_point]:
                continue
            checked[next_point] = True
            dist[next_point] = dist[cur_point] + 1
            q.append(next_point)
    return dist[K]


N, K = map(int, input().split())
max_size = 100001
checked = [False] * max_size
dist = [-1] * max_size
print(bfs(N))
