from collections import defaultdict


def get_mst_by_kruskal(N, edges):
    parent = dict()
    rank = dict()

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_u] = root_v
            if rank[root_u] == rank[root_v]:
                rank[root_u] += 1

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def make_set(node):
        parent[node] = node
        rank[node] = 0

    for i in range(N):
        make_set(i)

    w_sum = 0
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        node_u, node_v, w = edge
        if find(node_u) != find(node_v):
            union(node_u, node_v)
            w_sum += w

    return w_sum


T = int(input())
for _ in range(T):
    N, E = map(int, input().split())
    edge_list = list(map(int, input().split()))
    edges = list(zip(edge_list[::3], edge_list[1::3], edge_list[2::3]))
    print(get_mst_by_kruskal(N, edges))
