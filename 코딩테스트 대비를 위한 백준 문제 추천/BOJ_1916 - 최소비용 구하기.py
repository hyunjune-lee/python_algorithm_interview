# [0. 날짜]
# 2021.07.16(금요일)
# 문제 유형: 다익스트라
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import defaultdict
import heapq


def solution(N, bus_list, S, D):
    graph = defaultdict(list)
    cost_list = defaultdict(lambda: float("inf"))
    visited = defaultdict(lambda: False)

    for bus_start, bus_dest, bus_cost in bus_list:
        graph[bus_start].append((bus_dest, bus_cost))

    q = [(0, S)]
    while q:
        cost, node = heapq.heappop(q)
        if not visited[node]:
            visited[node] = True
            cost_list[node] = cost
            for next_node, add_cost in graph[node]:
                if not visited[next_node]:
                    delta_cost = cost + add_cost
                    heapq.heappush(q, (delta_cost, next_node))
    return cost_list[D]


N = int(input())
M = int(input())
bus_list = []
for _ in range(M):
    bus_list.append(list(map(int, input().split())))
S, D = map(int, input().split())
print(solution(N, bus_list, S, D))
