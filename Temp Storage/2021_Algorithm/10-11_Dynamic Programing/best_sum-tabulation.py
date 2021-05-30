def best_sum(m, nums):
    table = [None for _ in range(m + 1)]
    table[0] = []
    for i in range(m):
        if table[i] is not None:
            for x in nums:
                if i + x <= m:
                    best = table[i + x]
                    if best is None or len(best) > len(table[i]) + 1:
                        table[i + x] = table[i] + [x]
    return table[m]


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    nums = list(map(int, input().split()))
    res = best_sum(m, nums)
    if res is not None:
        print(len(res), " ".join(map(str, res)))
    else:
        print(-1)
