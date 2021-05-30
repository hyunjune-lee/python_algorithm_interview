import heapq
import copy


class Node:
    def __init__(self, level, tour):
        self.level = level
        self.tour = tour  # 일주여행경로
        self.bound = 0

    def __lt__(self, other):
        return self.bound < other.bound


# def contains(self, x):
#     for i in range(len(self.tour)):
#         if self.tour[i] == x:
#             return True
#     return False


def tsp(G):
    Q = []
    n = len(G) - 1
    root = Node(0, [1])
    root.bound = compute_bound(root, G)
    minLength = float("inf")
    heapq.heappush(Q, root)

    while Q:
        # ======================
        for q in Q:
            print(q.level, q.tour, q.bound, length(q.tour, G))
        print("--------------")
        # ======================

        node = heapq.heappop(Q)
        if node.bound < minLength:
            print("check1")
            for i in range(2, n + 1):
                if i in node.tour or G[node.tour[-1]][i] == -1:
                    continue

                next = copy.deepcopy(node)
                next.level += 1
                next.tour.append(i)

                if next.level == n - 2:
                    print("check2")
                    for k in range(2, n + 1):
                        if k not in next.tour:
                            next.tour.append(k)
                    next.tour.append(1)
                    new_length = length(next.tour, G)
                    if new_length < minLength:
                        minLength = new_length
                else:
                    print("check3")
                    next.bound = compute_bound(next, G)
                    if next.bound < minLength:
                        heapq.heappush(Q, next)

    return minLength


def compute_bound(node, G):
    # n = len(G)
    n = len(G) - 1
    bound = length(node.tour, G)
    for i in range(1, n + 1):
        # 행 제외
        if i in node.tour[:-1]:
            continue
        min = float("inf")
        for j in range(1, n + 1):
            if i == j:
                continue
            # 남은 경로가 있는데 바로 원점으로 돌아가는 경우 제외
            if i == node.tour[-1] and j == 1:
                continue
            # 열 제외
            if j in node.tour[1:]:
                continue
            # print("i, j:", i, j)
            if min > G[i][j]:
                min = G[i][j]
        bound += min
        print("min", min)
    return bound


def length(tour, G):
    length = 0
    prev = 1
    for i in range(len(tour)):
        if i != 0:
            prev = tour[i - 1]
        length += G[prev][tour[i]]
        prev = tour[i]
    print("length:", length)
    return length


N = int(input())
G = [[-1 for _ in range(N + 1)]]
for i in range(N):
    line = list(map(int, input().split()))
    G.append([-1] + [num if num != -1 else float("inf") for num in line])


print("==========")
for li in G:
    print(li)
result = tsp(G)
print(result)
