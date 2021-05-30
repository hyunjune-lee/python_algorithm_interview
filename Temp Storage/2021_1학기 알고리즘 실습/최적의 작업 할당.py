import heapq
import copy


class Node:
    def __init__(self, level, visited, n):
        self.level = int(level)
        self.bound = int(0)
        self.visited = visited
        self.unvisited = []
        for i in range(n):
            if i not in visited:
                self.unvisited.append(i)
        self.cost = 0

    def __lt__(self, other):
        return self.bound < other.bound


def get_min_bound_by_avail_visited(node, list):
    min_bound = float("inf")
    for avail_node in list:
        min_bound = min(min_bound, G[node][avail_node])
    return min_bound


def compute_bound(node):
    bound = node.cost
    for left_work in range(node.level + 1, n):
        bound += get_min_bound_by_avail_visited(left_work, node.unvisited)
    return bound


def get_next_node(node, next):
    next_node = copy.deepcopy(node)
    next_node.level = node.level + 1
    next_node.visited.append(next)
    next_node.unvisited.remove(next)
    next_node.cost += G[next_node.level][next]
    return next_node


# 넣기 직전에 복사해서, bound 계산해서 넣어주기(그래야 얕은 복사 문제, bound minheap이 제대로 작동)
def tsp(n):
    Q = []  # Node를 유지할 수 있는 priority queue (bound minHeap)
    for first_job in range(n):
        start_node = Node(0, [first_job], n)
        start_node.cost = G[0][first_job]
        start_node.bound = compute_bound(start_node)
        heapq.heappush(Q, start_node)
    mincost = float("inf")
    while Q:
        node = heapq.heappop(Q)
        if node.bound < mincost:
            for i in range(0, n):
                if i in node.visited:
                    continue
                next_node = get_next_node(node, i)
                if next_node.level == n - 1:
                    if next_node.cost < mincost:
                        mincost = next_node.cost
                else:
                    next_node.bound = compute_bound(next_node)
                    if next_node.bound < mincost:
                        heapq.heappush(Q, next_node)
    return mincost


t = int(input())
for _ in range(t):
    n = int(input())
    G = []
    for i in range(n):
        line = list(map(int, input().split()))
        G.append([num for num in line])
    print(tsp(n))
