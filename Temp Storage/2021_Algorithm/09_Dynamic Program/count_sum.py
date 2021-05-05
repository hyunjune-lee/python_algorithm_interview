def count_sum(m, nums):
    table = [0 for _ in range(m + 1)]
    table[0] = 1
    for i in range(m):
        if table[i] != 0:
            for x in nums:
                if i + x <= m:
                    table[i + x] += table[i]
    return table[m]


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    nums = list(map(int, input().split()))
    print(count_sum(m, nums))
