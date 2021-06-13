from collections import defaultdict
import heapq
# 개선 방향 => visited를 사용해서 방문하지 않은 노드만 넣어주기, 
# dist 배열을 이용해서 지금까지 구한 거리보다 짧은 경우에만 힙에추가

def dijkstra(edge_pairs, N, S, dest_list):
    graph = defaultdict(list)
    for u, v, w in edge_pairs:
        graph[u].append((v, w))

    dist_list = defaultdict(int)
    heap = [(0, S)]
    while heap:
        dist, node = heapq.heappop(heap)
        if node not in dist_list:
            dist_list[node] = dist
            for next_node, add_dist in graph[node]:
                #
                alt_dist = dist + add_dist
                heapq.heappush(heap, (alt_dist, next_node))

    ret = []
    for dest in dest_list:
        ret.append(dist_list[dest] if dest in dist_list else -1)
    return ret


T = int(input())
for _ in range(T):
    N, E, S, K, *d = map(int, input().split())
    edge_list = list(map(int, input().split()))
    edges = list(zip(edge_list[::3], edge_list[1::3], edge_list[2::3]))
    print(" ".join(map(str, dijkstra(edges, N, S, d))))
