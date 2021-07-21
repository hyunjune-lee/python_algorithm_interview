# [0. 날짜]
# 2021.07.20(화요일)
# 문제 유형: bfs, dfs
# 걸린 시간: 11분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import defaultdict
from collections import deque


def dfs(start_node):
    visited = [False for _ in range(N + 1)]
    stack = [start_node]
    while stack:
        cur_node = stack.pop()
        if not visited[cur_node]:
            visited[cur_node] = True
            for next_node in sorted(graph[cur_node], reverse=True):
                if not visited[next_node]:
                    stack.append(next_node)


from collections import deque


def bfs(start_node):
    visited = [False for _ in range(N + 1)]
    queue = deque([start_node])
    while queue:
        cur_node = queue.popleft()
        if not visited[cur_node]:
            print(cur_node, end=" ")
            visited[cur_node] = True
            for next_node in sorted(graph[cur_node]):
                if not visited[next_node]:
                    queue.append(next_node)


def solution():
    dfs(V)
    print()
    bfs(V)


N, M, V = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

solution()
