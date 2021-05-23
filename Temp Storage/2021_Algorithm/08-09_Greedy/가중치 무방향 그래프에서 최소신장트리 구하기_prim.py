import heapq


def get_mst_by_pirm(N, edges):
    nodes = []
    total_weight = 0
    visited = [False] * N
    mat = [[float("inf")] * N for _ in range(N)]
    for i in range(0, len(edges), 3):
        u, v, w = edges[i], edges[i + 1], edges[i + 2]
        mat[u][v] = mat[v][u] = w
    # weight, node
    heapq.heappush(nodes, (0, 0))

    while nodes:
        cur_weight, cur_node = heapq.heappop(nodes)
        if visited[cur_node]:
            continue
        total_weight += cur_weight
        visited[cur_node] = True
        for adjacent_node, weight in enumerate(mat[cur_node]):
            if not visited[adjacent_node] and weight != float("inf"):
                heapq.heappush(nodes, (weight, adjacent_node))
    return total_weight


T = int(input())
for _ in range(T):
    N, E = map(int, input().split())
    edges = list(map(int, input().split()))
    print(get_mst_by_pirm(N, edges))
