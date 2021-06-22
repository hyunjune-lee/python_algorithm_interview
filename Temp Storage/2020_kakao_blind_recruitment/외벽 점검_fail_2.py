# 시계 방향인지 반 시계 방향인지
# 완전 탐색으로?, 슬라이딩 윈도우?
# bfs
# dist가 큰 애부터 최대한 넓은 범위를 탐색하도록..
# 1개를 이용하는 경우, 2개를 이용하는 경우.. 검색 완료되면 종료되게 / 끝가지 해서 안되면 -1 return
# weak 15
# dist => 16 * 15
from collections import deque
import heapq


def solution(n, weak, dist):
    if max(dist) >= n:
        return 1
    dist.sort(reverse=True)
    q = []
    heapq.heappush(q, (0, len(weak), weak[:]))
    while q:
        d_i, not_visited_count, not_visited = heapq.heappop(q)
        if not not_visited:
            return d_i
        d = dist[d_i]
        for start_node in not_visited:
            # 시계 방향 탐색
            next_not_visited = not_visited[:]
            for fix_node in not_visited:
                if start_node <= fix_node <= start_node + d:
                    next_not_visited.remove(fix_node)
                if start_node + d >= n:
                    if 0 <= fix_node <= (start_node + d) % n:
                        next_not_visited.remove(fix_node)
            heapq.heappush(q, (d_i + 1, len(next_not_visited), next_not_visited))

            # 반시계 방향 탐색
            next_not_visited = not_visited[:]
            for fix_node in not_visited:
                if start_node >= fix_node >= start_node - d:
                    next_not_visited.remove(fix_node)
                if start_node - d < 0:
                    if n > fix_node >= n + (start_node - d):
                        next_not_visited.remove(fix_node)
            heapq.heappush(q, (d_i + 1, len(next_not_visited), next_not_visited))

    return -1


print(
    solution(
        12,
        [1, 5, 6, 10],
        [1, 2, 3, 4],
    )
)
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
