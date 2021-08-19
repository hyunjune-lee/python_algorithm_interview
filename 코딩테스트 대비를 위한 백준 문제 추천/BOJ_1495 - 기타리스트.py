n, s, m = map(int, input().split())
v_list = list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True

for y in range(1, n + 1):
    for x in range(m + 1):
        if dp[y - 1][x] == True:
            v = v_list[y - 1]
            if x + v <= m:
                dp[y][x + v] = True
            if x - v >= 0:
                dp[y][x - v] = True

res = -1
for v_index in range(len(dp[n]) - 1, -1, -1):
    if dp[n][v_index] == True:
        res = v_index
        break

print(res)
