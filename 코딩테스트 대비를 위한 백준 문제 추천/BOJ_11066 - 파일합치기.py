# [0. 날짜]
# 2021.08.14(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def sol(start, end):
    if dp[start][end] != -1:
        return dp[start][end]
    elif end - start == 0:
        return 0
    elif end - start == 1:
        dp[start][end] = files[start] + files[end]
        return dp[start][end]
    dp[start][end] = float("inf")
    for mid in range(start, end):
        left = sol(start, mid)
        right = sol(mid + 1, end)
        dp[start][end] = min(dp[start][end], left + right)

    dp[start][end] += sub_sum[end] - sub_sum[start - 1]

    return dp[start][end]


T = int(input())
for _ in range(T):
    K = int(input())
    files = [0] + list(map(int, input().split()))
    sub_sum = [0 for _ in range(K + 2)]
    for i in range(1, K + 1):
        sub_sum[i] = sub_sum[i - 1] + files[i]
    dp = [[-1 for _ in range(501)] for _ in range(501)]
    print(sol(1, K))
