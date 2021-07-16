# [0. 날짜]
# 2021.07.16(금요일)
# 문제 유형: mst
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 프림 알고리즘
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 처음에 q = [(0, start)]으로 시작하는 테크닉 생각
# [3. +개선 사항]
# 생각해보니 제일 최소 간선에서 굳이 시작할 필요X
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# while q 말고 for _ in range(E): 로 해서 틀림..
# 처음에 최소 간선을 연결해놓고 시작했는데 이때 간선의 한쪽 끝의 연결된 애들만 연결이 시작되어서 문제..
# => 사실 연결하고 시작할 필요도 X

import heapq
from collections import defaultdict


def solution(V, edges):
    graph = defaultdict(list)
    for start, end, weight in edges:
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    wegiht_sum = 0
    q = [(0, 1)]
    visited = [False for i in range(V + 1)]
    while q:
        weight, new_con_node = heapq.heappop(q)
        if not visited[new_con_node]:
            visited[new_con_node] = True
            wegiht_sum += weight
            for next_con_node, next_node_weight in graph[new_con_node]:
                if not visited[next_con_node]:
                    heapq.heappush(q, (next_node_weight, next_con_node))
    return wegiht_sum


V, E = map(int, input().split())
edges = []
for _ in range(E):
    start, end, weight = list(map(int, input().split()))
    edges.append((start, end, weight))

print(solution(V, edges))
