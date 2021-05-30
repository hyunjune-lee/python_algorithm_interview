# 너비 우선 알고리즘 - 성능 개선 거의 없음

import heapq


class Node:
    def __init__(self, level, profit, weight):
        self.level = int(level)
        self.profit = int(profit)
        self.weight = int(weight)
        self.bound = int(0)
        self.include = []

    def __lt__(self, other):
        return self.bound > other.bound


def get_max_profit_by_weight(n, items, limit_w, node):
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


def promising(n, items, limit_w, node):
    if node.weight >= limit_w:
        return False
    else:
        bound = get_max_profit_by_weight(n, items, limit_w, node)
        return bound > max_profit


def knapsack(n, items, limit_w):
    Q = []
    root = Node(0, 0, 0)
    root.bound = get_max_profit_by_weight(n, items, limit_w, root)
    heapq.heappush(Q, root)
    global max_profit
    while Q:
        node = heapq.heappop(Q)
        # node.bound = get_max_profit_by_weight(n, items, limit_w, node)
        if node.bound > max_profit:
            node.level += 1
            if node.level > len(items):
                continue

            # items[node.level]을 포함하지 않는 경우
            if promising(n, items, limit_w, node):
                next_node = Node(node.level, node.profit, node.weight)
                next_node.bound = get_max_profit_by_weight(n, items, limit_w, next_node)
                heapq.heappush(Q, Node(node.level, node.profit, node.weight))

            # items[node.level]을 포함하는 경우
            node.profit += items[node.level - 1][0]
            node.weight += items[node.level - 1][1]
            if promising(n, items, limit_w, node):
                if node.profit > max_profit:
                    max_profit = node.profit
                next_node = Node(node.level, node.profit, node.weight)
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
