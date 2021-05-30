import heapq
import copy


class Node:
    def __init__(self, level, tour, n):
        self.level = int(level)
        self.bound = int(0)
        self.tour = tour
        self.unvisited = [i for i in range(1, n)]
        self.length = 0

    def __lt__(self, other):
        return self.bound < other.bound


def get_min_bound_by_avail_tour(node, list):
    min_bound = float("inf")
    for avail_node in list:
        if avail_node != node:
            min_bound = min(min_bound, G[node][avail_node])
    return min_bound


# 현재 length 계산
# 현재 tour의 끝은 unvisited만 가능
# unvisited들은 unvisited에서 자기를 빼고, 1은 넣은 중에서 가능
def compute_bound(node):
    bound = node.length
    cur_last_tour = node.tour[-1]
    bound += get_min_bound_by_avail_tour(cur_last_tour, node.unvisited)
    for unvisited_node in node.unvisited:
        bound += get_min_bound_by_avail_tour(unvisited_node, node.unvisited + [0])
    return bound


def get_next_node(node, next):
    next_node = copy.deepcopy(node)
    next_node.level = node.level + 1
    next_node.tour.append(next)
    next_node.unvisited.remove(next)
    cur_last_tour = node.tour[-1]
    next_node.length += G[cur_last_tour][next]
    return next_node


def complete_tour(node):
    cur_last_tour = node.tour[-1]
    stopover = node.unvisited.pop()
    node.length += G[cur_last_tour][stopover]
    node.length += G[stopover][0]


# 넣기 직전에 복사해서, bound 계산해서 넣어주기(그래야 얕은 복사 문제, bound minheap이 제대로 작동)
def tsp(n):
    Q = []  # Node를 유지할 수 있는 priority queue (bound minHeap)
    root = Node(0, [0], n)
    root.bound = compute_bound(root)
    heapq.heappush(Q, root)
    minLength = float("inf")
    while Q:
        node = heapq.heappop(Q)
        if node.bound < minLength:
            for i in range(1, n):
                if i in node.tour:
                    continue
                if G[node.tour[node.level]][i] == float("inf"):
                    continue
                next_node = get_next_node(node, i)
                if next_node.level == n - 2:  # 2개남으면 경로가 다 정해진것, 마지막은 1이고, 남은 1개가 1로 가는 경유지
                    complete_tour(next_node)
                    if next_node.length < minLength:
                        minLength = next_node.length
                else:
                    next_node.bound = compute_bound(next_node)
                    if next_node.bound < minLength:
                        heapq.heappush(Q, next_node)
    return minLength


# t = int(input())
# for _ in range(t):
n = int(input())
G = []
for i in range(n):
    line = list(map(int, input().split()))
    G.append([num if num != -1 else float("inf") for num in line])
print(tsp(n))
