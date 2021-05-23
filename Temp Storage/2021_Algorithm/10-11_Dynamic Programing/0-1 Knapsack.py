def knapsack(n, limit_w, vals, weights):
    a = [[0 for _ in range(limit_w + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for x in range(limit_w + 1):
            if weights[i - 1] > x:
                a[i][x] = a[i - 1][x]
            else:
                a[i][x] = max(a[i - 1][x], a[i - 1][x - weights[i - 1]] + vals[i - 1])
    return a[n][limit_w]


t = int(input())
for _ in range(t):
    limit_w, n = map(int, input().split())
    item_list = list(map(int, input().split()))
    print(knapsack(n, limit_w, item_list[::2], item_list[1::2]))


# def knapsack(n, limit_w, item_list):
#     a = [[0 for _ in range(limit_w + 1)] for _ in range(n + 1)]
#     for item_idx in range(1, n + 1):
#         cur_v = item_list[2 * (item_idx - 1)]
#         cur_w = item_list[2 * (item_idx - 1) + 1]
#         for w in range(1, limit_w + 1):
#             if w - cur_w >= 0:
#                 a[item_idx][w] = max(a[item_idx - 1][w], cur_v + a[item_idx - 1][w - cur_w])
#             else:
#                 a[item_idx][w] = a[item_idx - 1][w]
#     return a[n][w]


# t = int(input())
# for _ in range(t):
#     limit_w, n = map(int, input().split())
#     item_list = list(map(int, input().split()))
#     print(knapsack(n, limit_w, item_list))


# # itemlist 2504ms
# def knapsack(n, limit_w, item_list):
#     a = [[0 for _ in range(limit_w + 1)] for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for x in range(limit_w + 1):
#             cur_i = 2 * (i - 1)
#             if item_list[cur_i + 1] > x:
#                 a[i][x] = a[i - 1][x]
#             else:
#                 a[i][x] = max(a[i - 1][x], a[i - 1][x - item_list[cur_i + 1]] + item_list[cur_i])
#     return a[n][limit_w]


# t = int(input())
# for _ in range(t):
#     limit_w, n = map(int, input().split())
#     item_list = list(map(int, input().split()))
#     print(knapsack(n, limit_w, item_list))
