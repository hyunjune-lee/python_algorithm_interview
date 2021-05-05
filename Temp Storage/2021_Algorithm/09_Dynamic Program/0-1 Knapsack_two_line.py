def knapsack(n, limit_w, item_list):
    a = [[0 for _ in range(limit_w + 1)] for _ in range(2)]
    for item_idx in range(1, n + 1):
        cur_i = (item_idx + 1) % 2
        before_i = (item_idx) % 2
        cur_v = item_list[2 * (item_idx - 1)]
        cur_w = item_list[2 * (item_idx - 1) + 1]
        for w in range(1, limit_w + 1):
            if w - cur_w >= 0:
                a[cur_i][w] = max(a[before_i][w], cur_v + a[before_i][w - cur_w])
            else:
                a[cur_i][w] = a[before_i][w]
    return a[(n + 1) % 2][w]


t = int(input())
for _ in range(t):
    limit_w, n = map(int, input().split())
    item_list = list(map(int, input().split()))
    print(knapsack(n, limit_w, item_list))

# 1968ms
# def knapsack(n, limit_w, vals, weights):
#     a = [[0 for _ in range(limit_w + 1)] for _ in range(2)]
#     for i in range(1, n + 1):
#         cur_i = (i + 1) % 2
#         before_i = (i) % 2
#         for w in range(1, limit_w + 1):
#             if w - weights[i - 1] >= 0:
#                 a[cur_i][w] = max(a[before_i][w], vals[i - 1] + a[before_i][w - weights[i - 1]])
#             else:
#                 a[cur_i][w] = a[before_i][w]
#     return a[(n + 1) % 2][w]


# t = int(input())
# for _ in range(t):
#     limit_w, n = map(int, input().split())
#     item_list = list(map(int, input().split()))
#     vals = item_list[::2]
#     weights = item_list[1::2]
#     print(knapsack(n, limit_w, vals, weights))
