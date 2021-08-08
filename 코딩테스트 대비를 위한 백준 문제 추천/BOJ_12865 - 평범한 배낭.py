# [0. 날짜]
# 2021.07.23(금요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# y는 각 물건, x 는 무게이다.
# 첫번째 줄은 첫번째 물건이 들어갈 수 있을 때부터 해당 가치로 채워넣고
# 두번째 줄부터 첫번째 물건을 넣을지, 두번째 물건을 넣을지 생각
# 2차원 배열을 진행하면서
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

for y in range(1, n + 1):
    w, v = map(int, input().split())
    for x in range(k + 1):
        if x < w:
            dp[y][x] = dp[y - 1][x]
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - w] + v)
print(dp[n][k])
