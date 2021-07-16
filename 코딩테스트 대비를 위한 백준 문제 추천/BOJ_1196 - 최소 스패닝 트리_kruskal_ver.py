# [0. 날짜]
# 2021.07.17(토요일)
# 문제 유형: mst
# 걸린 시간: 25분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import defaultdict


def solution(V, edges):
    root = [v_i for v_i in range(V + 1)]
    rank = [0 for _ in range(V + 1)]

    def find(node):
        if root[node] != node:
            root[node] = find(root[node])
        return root[node]

    def union(a, b):
        if (root_a := find(a)) != (root_b := find(b)):
            if rank[root_a] > rank[root_b]:
                root[root_b] = root_a
            else:
                root[root_a] = root_b
                if rank[root_a] == rank[root_b]:
                    rank[root_b] += 1
            return True
        return False

    mst_weight = 0
    for weight, start, end in (edges := sorted(edges)) :
        if union(start, end):
            mst_weight += weight

    return mst_weight


V, E = map(int, input().split())
edges = []
for _ in range(E):
    start, end, weight = list(map(int, input().split()))
    edges.append((weight, start, end))

print(solution(V, edges))
