# 뭔가 리프노드에서 가운데로 모이는 느낌인데..
# 최소 높이 트리 응용?
# 아니다 이건 트리간의 거리를 구하고 해당 트리의 곱이 최소가 되는 곳
# 그 곳에서 자신의 것을 빼고 나머지 그 곱의 합을 더하면 됨
# [last]
# 리프노드 중에 가중치가 짧은 애들을 없애면 된다. 실시간
# 아 중간에 사라지는 경우 쌍소멸!!
# 0을 없애야하나? => X
import collections
import heapq

def solution(a, edges):
    if sum(a) != 0:
        return -1
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    leaves_heap = []
    node_count = len(a)
    for i in range(node_count):
        if len(graph[i]) == 1:
            leaves_heap.append((a[i], i))
    heapq.heapify(leaves_heap)
    weight = 0
    while node_count > 1:
        leaf_weight, leaf = heapq.heappop(leaves_heap)
        neighbor = graph[leaf].pop()
        graph[neighbor].remove(leaf)
        a[neighbor] += leaf_weight
        weight += abs(leaf_weight)
        if len(graph[neighbor]) == 1:
            if a[neighbor] != 0:
                heapq.heappush(leaves_heap, (a[neighbor], neighbor))
        node_count -= 1

    return weight
