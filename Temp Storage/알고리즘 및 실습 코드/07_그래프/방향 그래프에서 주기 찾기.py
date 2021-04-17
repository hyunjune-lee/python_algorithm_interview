from collections import defaultdict


def make_graph(pairs):
    graph = defaultdict(list)
    for a, b in pairs:
        graph[a].append(b)
    return graph


def is_cycle(N, pairs):
    visited = [False for _ in range(N)]
    graph = make_graph(pairs)

    def dfs(node):
        if node in traced:
            return True
        if node in visited:
            return False
        traced.add(node)
        for next in graph[node]:
            if dfs(next):
                return True
        traced.remove(node)
        visited.add(node)

    traced = set()
    visited = set()
    for node in range(N):
        if dfs(node):
            return "true"
    return "false"


T = int(input())
for _ in range(T):
    N, E = list(map(int, input().split()))
    edges = list(map(int, input().split()))
    pairs = list(zip(edges[::2], edges[1::2]))
    print(is_cycle(N, pairs))
