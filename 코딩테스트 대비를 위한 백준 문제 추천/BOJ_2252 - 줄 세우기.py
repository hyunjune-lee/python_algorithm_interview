# [0. 날짜]
# 2021.07.17(토요일)
# 문제 유형: 위상정렬
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1. 주어진 비교를 통해 graph 생성
# 2. DFS를 통해 탐색 후 끝에서부터 돌아오면서
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def dfs(start_node, visited):
    if len(graph[start_node]) == 0:
        res.append(start_node)
        return
    for con_node in graph[start_node]:
        if visited[con_node]:
            continue
        visited[con_node] = True
        dfs(con_node, visited)
    res.append(start_node)


def solution():
    visited = [False for v in range(N + 1)]
    for start_node in range(1, N + 1):
        if in_degree[start_node] == 0:
            dfs(start_node, visited)


N, M = map(int, input().split())
graph = defaultdict(list)
in_degree = [0 for t in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

res = []
solution()
for i in range(N - 1, -1, -1):
    print(res[i], end=" ")
