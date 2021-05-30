# 최고 우선 검색 분기 한정 가지치기
import heapq
import copy

class Node:
    def __init__(self, level, profit, weight):
        self.level = int(level)
        self.profit = int(profit)
        self.weight = int(weight)
        self.bound = int(0)

    def __lt__(self, other):
        return self.bound > other.bound


def get_max_profit_by_weight(n, items, limit_w, node):
    if node.weight >= limit_w:
        return 0  # 이거 한개로 시간초 차이 엄청남
    bound = node.profit
    total_weight = node.weight
    next_idx = node.level
    while next_idx < n and total_weight + items[next_idx][1] <= limit_w:
        total_weight += items[next_idx][1]
        bound += items[next_idx][0]
        next_idx += 1
    if next_idx < n:
        bound += (limit_w - total_weight) * (items[next_idx][0] / items[next_idx][1])

    return bound


def knapsack(n, items, limit_w):
    Q = []
    root = Node(0, 0, 0)
    root.bound = get_max_profit_by_weight(n, items, limit_w, root)
    heapq.heappush(Q, root)
    global max_profit
    while Q:
        node = heapq.heappop(Q)
        if node.bound > max_profit:
            node.level += 1
            if node.level > len(items):
                continue

            if node.bound > max_profit:
                next_node = copy.copy(node)
                next_node.bound = get_max_profit_by_weight(n, items, limit_w, next_node)
                heapq.heappush(Q, next_node)

            node.profit += items[node.level - 1][0]
            node.weight += items[node.level - 1][1]
            if node.weight <= limit_w and node.profit > max_profit:
                max_profit = node.profit
            if node.bound > max_profit:
                next_node = copy.copy(node)
                next_node.bound = get_max_profit_by_weight(n, items, limit_w, next_node)
                heapq.heappush(Q, next_node)


t = int(input())
for _ in range(t):
    limit_w, n = map(int, input().split())
    item_list = list(map(int, input().split()))
    items = list(zip(item_list[::2], item_list[1::2]))  # item = (profit, weight)
    items.sort(key=lambda x: -(x[0] / x[1]))
    max_profit = 0
    knapsack(n, items, limit_w)
    print(max_profit)
