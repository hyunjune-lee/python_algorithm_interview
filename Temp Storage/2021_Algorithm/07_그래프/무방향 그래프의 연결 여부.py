from collections import defaultdict

# 개선 방향 -> 굳이 component를 유지할 필욘 없음


def bfs(graph, visited, i):
    visited[i] = True
    component = [i]
    q = [i]
    while q:
        node = q.pop(0)
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                component.append(next)
    return component


def make_graph(pairs):
    graph = defaultdict(list)
    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)
    return graph


def get_component(N, pairs):
    components = []
    visited = [False for _ in range(N)]
    graph = make_graph(pairs)

    for i in range(N):
        if not visited[i]:
            components.append(bfs(graph, visited, i))

    return (len(components), len(max(components, key=len)))


T = int(input())
for _ in range(T):
    N, E = list(map(int, input().split()))
    edges = list(map(int, input().split()))
    pairs = list(zip(edges[::2], edges[1::2]))
    print(" ".join(map(str, get_component(N, pairs))))
