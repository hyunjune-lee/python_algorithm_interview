def get_max_profit_by_weight(n, items, limit_w, cur_profit, cur_weight, next_idx):
    bound = cur_profit
    total_weight = cur_weight
    while next_idx < n and total_weight + items[next_idx][1] <= limit_w:
        total_weight += items[next_idx][1]
        bound += items[next_idx][0]
        next_idx += 1
    if next_idx < n:
        bound += (limit_w - total_weight) * (items[next_idx][0] / items[next_idx][1])

    return bound


def promising(n, items, limit_w, cur_profit, cur_weight, idx):
    if cur_weight >= limit_w:
        return False
    else:
        bound = get_max_profit_by_weight(n, items, limit_w, cur_profit, cur_weight, idx + 1)
        global max_profit
        return bound > max_profit


def knapsack(n, items, include, limit_w, cur_profit, cur_weight, idx):
    global max_profit
    if cur_weight <= limit_w and cur_profit > max_profit:
        max_profit = cur_profit
        solution = include
    if promising(n, items, limit_w, cur_profit, cur_weight, idx):
        include[idx + 1] = True
        knapsack(
            n,
            items,
            include,
            limit_w,
            cur_profit + items[idx + 1][0],
            cur_weight + items[idx + 1][1],
            idx + 1,
        )
        include[idx + 1] = False
        knapsack(n, items, include, limit_w, cur_profit, cur_weight, idx + 1)
    return max_profit


t = int(input())
for _ in range(t):
    limit_w, n = map(int, input().split())
    item_list = list(map(int, input().split()))
    items = list(zip(item_list[::2], item_list[1::2]))  # item = (profit, weight)
    items.sort(key=lambda x: -(x[0] / x[1]))
    include = [False for _ in range(n)]
    max_profit = 0
    knapsack(
        n,
        items,
        include,
        limit_w,
        0,
        0,
        -1,
    )
    print(max_profit)
