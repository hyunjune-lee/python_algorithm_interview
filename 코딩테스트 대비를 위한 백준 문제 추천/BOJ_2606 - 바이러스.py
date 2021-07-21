# [0. 날짜]
# 2021.07.21(수요일)
# 문제 유형: bfs, dfs
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import deque

n = int(input())
adj = int(input())

computer = [[] for _ in range(n + 1)]
for _ in range(adj):
    x, y = map(int, input().split())
    computer[x].append(y)
    computer[y].append(x)


def dfs():
    q = deque([1])
    visited = []
    while q:
        node = q.pop()
        if node not in visited:
            visited.append(node)
            q.extend(computer[node])
    print(len(visited) - 1)


dfs()
